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
headers = {"Authorization": f"Bearer {github_token}"}

projets_raw = os.getenv("PROJECTS", "")  # Valeur par défaut si la variable est absente
projets = projets_raw.split(",") if projets_raw else []


print("Liste des projets à surveiller :", projets)
for project in projets:
    print(f"------------ {project}")

    gh_url = f"https://api.github.com/repos/{project}/tags"

    print(f"-> {gh_url}")
    response = requests.get(gh_url) 
    if response:
        for release in response.json():
            xtr_release_name=release.get('name', headers=headers)
            print(xtr_release_name)
            data_commit = requests.get(release.get('commit').get('url'), headers=headers) 
            pprint.pprint(data_commit.json())


            quit()
            #xtr_release_author=data_commit.json().get('committer').get('name')
            #xtr_release_date=data_commit.json().get('committer').get('date')

            #print (f"{project} - {xtr_release_name} from {xtr_release_author} at {xtr_release_date}")
    else:
        print(f"ERROR CODE {response.status_code} requesting")
    
    #pprint.pprint(response.json())
    