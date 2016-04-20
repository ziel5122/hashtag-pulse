import austin_oauth
from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


class listener(StreamListener):

    def on_data(self, data):
        j = json.loads(data)
        keys = j.keys()
        for i in range (0, len(keys)):
            if keys[i] == 'lang':
                if j[keys[i]] == 'en':
                    print j[keys[i]]
        print(data.lang)
        return(True)

    def on_error(self, status):
        print status

oauth = austin_oauth.getOAuth()

twitterStream = Stream(oauth, listener())
twitterStream.sample()
#twitterStream.filter(track=["dog"])

'''
api = API(auth)
public_tweets = api.home_timeline()

for tweet in public_tweets:
    print tweet
'''

