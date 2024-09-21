import tweepy
from dotenv import dotenv_values
import tweepy.cursor

keys = dotenv_values()
consumer_key = keys["CONSUMER_KEY"]
consumer_secret = keys["CONSUMER_SECRET"]
access_token = keys["ACCESS_TOKEN"]
access_secret = keys["ACCESS_SECRET"]


auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.home_timeline).items(10):
    print(tweet.text)