import austin_oauth
import json
from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import stream_classifier

classifierInstance = stream_classifier.generate_classifier()


class listener(StreamListener):

    def on_status(self, data):
        j = data._json
        if j['lang'] == 'en':
            stream_classifier.classify_tweet(data.text, classifierInstance)
        return(True)

    def on_error(self, status):
        if status == 401:
            print "make sure VM and host clock are in sync"
        else:
            print status

client = MongoClient('argon.plttn.me', 27017)
db = client['hashtag-pulse']
db.authenticate('pulseUser', '+xCh4VduYDX1cG')

oauth = austin_oauth.getOAuth()


musicianStream = Stream(oauth, listener()) #sets up listener
musicianStream.filter(track=['taylor swift'])

'''
api = API(auth)
public_tweets = api.home_timeline()

for tweet in public_tweets:
    print tweet
'''
