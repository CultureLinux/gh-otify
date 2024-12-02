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

projets_raw = os.getenv("PROJECTS", "")
projects = projets_raw.split(",") if projets_raw else []
history_path = "tracking"

discord_token = os.getenv("DISCORD_BOT_TOKEN", "")
discord_channel = int(os.getenv("DISCORD_CHANNEL_IDS", ""))

bsky_account = os.getenv("BSKY_ACCOUNT", "")
bsky_password = os.getenv("BSKY_PASSWORD", "")



#from vault.notif_bsky import NotifBsky
#bsky = NotifBsky(bsky_account,bsky_password)
#bsky.test("Aujourd'hui ca va tomber #snow")
#quit()
###########################
### VARS
##########################

send_notification = True

###########################
### EXEC
##########################

pprint.pprint(projects)

gh_crawler = GitHubReleases(github_token,projects,history_path)
all_notifs = gh_crawler.get_all_releases()

if len(all_notifs) > 0 and send_notification == True:

    if discord_channel != '' and discord_token != '':
        print('Discord notification detected')
        from vault.notif_discord import NotifDiscord
        discord = NotifDiscord(discord_token,discord_channel)

        for proj, tag in all_notifs.items():
            print(f"[{proj}] {tag}")
            discord.notif(proj,tag)

    if bsky_account != "" and bsky_password != "" :
        print('Bsky notification detected')
        from vault.notif_bsky import NotifBsky
        bsky = NotifBsky(bsky_account,bsky_password)

        for proj, tag in all_notifs.items():
            print(f"[{proj}] {tag}")
            bsky.post(proj,tag)

else:
    print("no notifications")

print("--" * 30)

pprint.pprint(all_notifs)

