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

discord_token = os.getenv("DISCORD_BOT_TOKEN", "")
discord_channel = int(os.getenv("DISCORD_CHANNEL_IDS", ""))


pprint.pprint(projects)

gh_release = GitHubReleases(github_token,projects,history_path)
all_notifs = gh_release.get_all_releases()


if discord_channel != '' and discord_token != '' and len(all_notifs) > 0:
    print('Discord notification detected')
    from vault.notif_discord import NotifDiscord
    discord = NotifDiscord(discord_token,discord_channel)

    for proj, tag in all_notifs.items():
        print(f"[{proj}] {tag}")
        discord.notif(f"[{proj}] {tag}")


else:
    print("no notif and/or no discord configuration")

print("--" * 30)

pprint.pprint(all_notifs)

