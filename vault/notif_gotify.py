import requests

class NotifGotify:
    def __init__ (self,gotify_url,gotify_token):
        self.gotify_url = gotify_url
        self.gotify_token = gotify_token

    def post (self,project,tags):

        for tag in tags:
            
            post = f"Le tag {tag} vient d'apparaitre sur le project {project} \n Voir le changelog https://github.com/{project}/releases/tag/{tag}"
            data = {
                "title": project,
                "message": post,
                "priority": 5
            }
            response = requests.post(self.gotify_url, headers={"X-Gotify-Key": self.gotify_token}, json=data)









