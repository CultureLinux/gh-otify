import tweepy

class NotifX:
    def __init__ (self,x_api_key,x_api_secret,x_access_token,x_access_secret):
        self.client = tweepy.Client(consumer_key=x_api_key,
                       consumer_secret=x_api_secret,
                       access_token=x_access_token,
                       access_token_secret=x_access_secret)
        

    def test (self,string):
        try:
            self.client.create_tweet(text=string)
            print("Tweet posté avec succès !")
        except tweepy.TweepyException as e:
            print(f"Erreur : {e}")


    def post (self,project,tags):

        for tag in tags:

            post = f"Le tag {tag} vient d'apparaitre sur le project {project} \n Voir le changelog https://github.com/{project}/releases/tag/{tag}"
            self.client.create_tweet(text=post)







