import austin_oauth
import json
from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import TweetClassifier2 as tc
import csv
import re
import cPickle

clf_file = open('tweet_classifier_small.pickle','rb')
classifierObj = cPickle.load(clf_file)
clf_file.close()
ratioList = [0,0,0]
tweetRolling = 0
oldTweetTotal = 0

def adjustList(emotion, emotionList):

    if emotion == '0': #negative emotion
        emotionList[0] += 1
    if emotion == '2': #neutral emotion
        emotionList[1] += 1
    if emotion == '4': #postive emotion
        emotionList[2] += 1

    return emotionList

def tweetsPer10(tweetTotal):
    globalTweetTotal = tweetTotal
    pass



def calculateRatio(emotionList, tweetTotal):
    ratioList[0] = float(emotionList[0]) / tweetTotal
    ratioList[1] = float(emotionList[1]) / tweetTotal
    ratioList[2] = float(emotionList[2]) / tweetTotal
    pass


def setTweetTotal(arg):
    globalTweetTotal = arg
    pass


class listener(StreamListener):
    tweetTotal = 0
    emotionList = [0,0,0]


    def on_status(self, data):
        j = data._json
        if j['lang'] == 'en':
            tweetData = tc.strip_punctuation(data.text)
            emotion =  classifierInstance.classify(classifierObj.extract_features(tweetData.split()))
            self.tweetTotal += 1
            self.emotionList = adjustList(emotion, self.emotionList)
            setTweetTotal(self.tweetTotal)
            calculateRatio(self.emotionList, self.tweetTotal)
            print ratioList
        return(True)

    def on_error(self, status):
        if status == 401:
            print "make sure VM and host clock are in sync"
        else:
            print status


oauth = austin_oauth.getOAuth()

classifierInstance = classifierObj.getClassifier()

streamInstance = Stream(oauth, listener()) #sets up listener


def startStream(search='dogs'):
    streamInstance.filter(track=[search],async=True)
    pass


def stopStream():
    streamInstance.disconnect()
    pass

#musicianStream.disconnect() to close stream
