from dotenv import load_dotenv
import os
import requests
import pprint
from datetime import datetime

###########################
### ENV
##########################

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN", "")
headers = {"Authorization": f"Bearer {github_token}","Content-Type": "application/json"}

projets_raw = os.getenv("PROJECTS", "")  # Valeur par défaut si la variable est absente
projets = projets_raw.split(",") if projets_raw else []


###########################
### VARS
##########################

def contains_substring(file_path, substring):
    with open(file_path, "r") as file:
        for line in file:
            if substring in line:  # Vérifie si le sous-ensemble est dans la ligne
                return True
    return False  # Si le sous-ensemble n'est pas trouvé





###########################
### Main
##########################

print("Liste des projets à surveiller :", projets)
for project in projets:
    print(f"------------ {project}")
    history_file="tracking/{}".format(project.replace('/','-'))

    print(f"history in  {history_file}")
    

    gh_url = f"https://api.github.com/repos/{project}/tags"

    print(f"-> {gh_url}")
    response = requests.get(gh_url, headers=headers) 
    if response:

        pprint.pprint(response.links)

        for release in response.json():
            xtr_release_name=release.get('name')
            print(f"Searching *{xtr_release_name}*")
            test_tag = contains_substring(history_file,xtr_release_name)

            if test_tag:
                print("Tag deja traité")
                continue

            data_commit = requests.get(release.get('commit').get('url'), headers=headers) 
            
            if data_commit:
                try:
                    data = data_commit.json() 
                except ValueError:
                    print("La réponse n'est pas au format JSON")

                xtr_release_author=data.get('commit').get('author').get('name')
                xtr_release_author_email=data.get('commit').get('author').get('email')
                xtr_release_date=data.get('commit').get('committer').get('date')

                full_info = f"[{xtr_release_name}] from {xtr_release_author} {xtr_release_author_email} at {xtr_release_date}"
                print(full_info)
                tracking_file = open(history_file, "a")
                tracking_file.write(full_info+"\n")

            else:
                print(f"ERROR CODE {response.status_code} requesting commit")
                quit()


    else:
        print(f"ERROR CODE {response.status_code} requesting project")
        quit()
    

    