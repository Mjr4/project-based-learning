import tweepy
from dotenv import dotenv_values
import tweepy.client

class tweeterClient():
    def __init__(self):
        keys = dotenv_values()
        self.CONSUMER_KEY = keys["CONSUMER_KEY"]
        self.CONSUMER_SECRET = keys["CONSUMER_SECRET"]
        self.ACCESS_TOKEN = keys["ACCESS_TOKEN"]
        self.ACCESS_SECRET = keys["ACCESS_SECRET"]
        self.BEARER_TOKEN = keys["BEARER_TOKEN"]
        
        self.client = tweepy.Client(
            self.BEARER_TOKEN,
            self.CONSUMER_KEY,
            self.CONSUMER_SECRET,
            self.ACCESS_TOKEN,
            self.ACCESS_SECRET)
    

    def tweet(self, message=""):
        response = self.client.create_tweet(
            text=message
        )
        return response
    
if __name__=="__main__":
    tweeter_client = tweeterClient()
    response = tweeter_client.tweet("this tweet is also using tweepy")
    print(f"https://twitter.com/user/status/{response.data['id']}")