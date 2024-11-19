import requests
import os

class GitHubReleases:
    def __init__(self, token, projects,history_path):
        self.token = token
        self.projects = projects
        self.path = history_path
        self.notifs = {}
        
    def setUrl(self,github_project):
        self.base_url = f"https://api.github.com/repos/{github_project}/tags"

    def getUrl(self):
        return self.base_url
    
    def set_headers(self):
        self.headers = {"Authorization": f"Bearer {self.token}","Content-Type": "application/json"}

    def tracking_tag(self,project,tag):
        with open(project, "r") as file:
            for line in file:
                if tag in line:
                    return True
        return False

    def get_tag_data(self,project,tag,commit):
        data_commit = requests.get(commit, headers=self.headers) 
        if data_commit.status_code == 200:
            try:
                data = data_commit.json() 
            except ValueError:
                print("La réponse n'est pas au format JSON")
                quit()
        else:
            print(f"Erreur {data_commit.status_code}: {data_commit.text}")
            quit()

        xtr_release_author=data.get('commit').get('author').get('name')
        xtr_release_author_email=data.get('commit').get('author').get('email')
        xtr_release_date=data.get('commit').get('committer').get('date')

        full_info = f"[{tag}] from {xtr_release_author} {xtr_release_author_email} at {xtr_release_date}"
        print(full_info)

        if project not in self.notifs:
            self.notifs[project] = []

        self.notifs[project].append(tag)

        tracking_file = open(f"{self.path}/{project.replace('/','-')}", "a")
        tracking_file.write(full_info+"\n")
        tracking_file.close()

    def get_all_releases(self):
        self.set_headers()

        for project in self.projects:
            self.setUrl(project)
            tags = []
            
            print(project)
            print(self.getUrl())

            history_file = f"{self.path}/{project.replace('/','-')}"
            if not os.path.exists(history_file):
                os.mknod(history_file)

            url = self.getUrl()
            while url:
                print(f"GET [{url}]")
                response = requests.get(url, headers=self.headers)
                
                if response.status_code == 200:
                    tags_data = response.json()
                    tags.extend(tags_data)
                    
                    for tag in tags_data:
                        xtr_release_name=tag.get('name')
                        print(f"Searching *{xtr_release_name}*")
                       
                        is_tag_crawled = self.tracking_tag(history_file,xtr_release_name)
                        
                        if is_tag_crawled == True:
                            print("Already crawled")
                        else: 

                            self.get_tag_data(project,xtr_release_name,tag.get('commit').get('url'))
                            

                    # Vérifier s'il y a une page suivante (utilisation des liens 'next')
                    if 'next' in response.links:
                        url = response.links['next']['url']
                    else:
                        break
                else:
                    print(f"Erreur {response.status_code}: {response.text}")
                    break

        return self.notifs    

    def display_releases(self):
        releases = self.get_all_releases()
        print("-" * 50)
        print(f"Nombre total de releases récupérées : {len(releases)}")
        for release in releases:
            print(f"Version : {release['name']}")
            print(f"Date de publication : {release['published_at']}")
            print(f"URL : {release['html_url']}")
            print("-" * 50)