import tweepy
import json

auth = tweepy.OAuthHandler("XRe0UVLvYnb0BFHRUICp4d1JP", "g9Ckq3jbn7VKLyPxmDXbUu2uPFd3FMki6u6KmMXy32uw19HZpV") #consumer_key, consumer_secret
auth.set_access_token("71678799-rku0MuMXcJgYRrT9Sm9xvoZflI7awxAnT3rZSEz6V", "YSTw0vK8Mg1kpFSsYa8VtKwVg4U2JubDXfAjVzE4486uy")

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

public_tweets = api.home_timeline()
print len(public_tweets)
print type(public_tweets[0])

    #print type(item)
    #print ""

testTweet = api.get_status(720378253773381633)
#data = json.dumps(testTweet._json)

print testTweet['coordinates']

for key in testTweet.keys():
    print key
    

