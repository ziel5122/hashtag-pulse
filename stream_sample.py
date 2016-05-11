import austin_oauth
import json
from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from TweetClassifier import TweetClassifier

classifier = TweetClassifier(True)

class listener(StreamListener):

    def on_status(self, data):
        j = data._json
        if j['lang'] == 'en':
            print classifier.classify(data.text)
        return(True)

    def on_error(self, status):
        if status == 401:
            print "make sure VM and host clock are in sync"
        else:
            print status

oauth = austin_oauth.getOAuth()


musicianStream = Stream(oauth, listener()) #sets up listener
musicianStream.sample()

'''
api = API(auth)
public_tweets = api.home_timeline()

for tweet in public_tweets:
    print tweet
'''
