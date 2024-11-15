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



print("Liste des projets à surveiller :", projets)
for project in projets:
    print(f"------------ {project}")
    tracking_file = open("tracking/{}".format(project.replace('/','-')), "w")

    gh_url = f"https://api.github.com/repos/{project}/tags"

    print(f"-> {gh_url}")
    response = requests.get(gh_url, headers=headers) 
    if response:
        for release in response.json():
            xtr_release_name=release.get('name')
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
                tracking_file.write(full_info)
                exit()
            else:
                print(f"ERROR CODE {response.status_code} requesting")


    else:
        print(f"ERROR CODE {response.status_code} requesting")
    
    #pprint.pprint(response.json())
    