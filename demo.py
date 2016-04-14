import tweepy
import json
import austin_oauth

oauth = austin_oauth.getOAuth()

api = tweepy.API(oauth, parser=tweepy.parsers.JSONParser())

tweets = {}

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet['id']
    
print " "

