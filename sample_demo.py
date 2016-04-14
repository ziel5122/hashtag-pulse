import austin_oauth
from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

class listener(StreamListener):

    def on_data(self, data):
        print(data)
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

