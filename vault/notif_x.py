import tweepy

class NotifX:
    def __init__ (self,x_api_key,x_api_secret,x_access_token,x_access_secret):
        auth = tweepy.OAuthHandler(x_api_key, x_api_secret)
        auth.set_access_token(x_access_token, x_access_secret)
        self.api = tweepy.API(auth)

    def post (self,project,tags):

        for tag in tags:

            post = f"Le tag {tag} vient d'apparaitre sur le project {project} \n Voir le changelog https://github.com/{project}/releases/tag/{tag}"
            self.api.update_status(post)







