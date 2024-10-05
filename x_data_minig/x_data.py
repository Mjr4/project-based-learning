import tweepy
from dotenv import dotenv_values
import tweepy.client

keys = dotenv_values()
CONSUMER_KEY = keys["CONSUMER_KEY"]
CONSUMER_SECRET = keys["CONSUMER_SECRET"]
ACCESS_TOKEN = keys["ACCESS_TOKEN"]
ACCESS_SECRET = keys["ACCESS_SECRET"]
BEARER_TOKEN = keys["BEARER_TOKEN"]

client = tweepy.Client(BEARER_TOKEN,CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

response = client.create_tweet(
    text="This Tweet was Tweeted using Tweepy and Twitter API v2!"
)
print(f"https://twitter.com/user/status/{response.data['id']}")