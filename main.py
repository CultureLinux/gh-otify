from dotenv import load_dotenv
import os
import requests
import pprint
from datetime import datetime

from vault.github_releases import  GitHubReleases
###########################
### ENV
##########################

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN", "")

projets_raw = os.getenv("PROJECTS", "")  # Valeur par défaut si la variable est absente
projects = projets_raw.split(",") if projets_raw else []
history_path = "tracking"

pprint.pprint(projects)

gh_release = GitHubReleases(github_token,projects,history_path)

all_tags = gh_release.get_all_releases()

pprint.pprint(all_tags)

