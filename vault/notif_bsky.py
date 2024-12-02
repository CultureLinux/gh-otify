import requests
import json
from datetime import datetime, timezone
from atproto import Client, client_utils

class NotifBsky:
    def __init__ (self,bsky_account,bsky_password):
        self.client = Client()
        self.client.login(bsky_account, bsky_password)

    def test (self,message):

        tb = client_utils.TextBuilder()
        tb.text(message)
        #tb.link(url, url)
        tb.text(' .')

        self.client.send_post(tb)

    def post (self,project,tags):
        now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


        for tag in tags:

            post = f"Le tag {tag} vient d'apparaitre sur le project {project} \n "
            tb = client_utils.TextBuilder()
            tb.text(post)
            tb.link("Voir le changelog ", f"https://github.com/{project}/releases/tag/{tag}")


            self.client.send_post(tb)






