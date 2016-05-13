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
globalCount = 20 #normalized
lastCount = 0
globalTweetTotal = 0
globalEmotionList = [0,0,0]



def adjustList(emotion, emotionList):

    if emotion == '0': #negative emotion
        emotionList[0] += 1
    if emotion == '2': #neutral emotion
        emotionList[1] += 1
    if emotion == '4': #postive emotion
        emotionList[2] += 1

    return emotionList


def calculateRatio():
    global globalCount
    global globalEmotionList
    ratioList[0] = float(globalEmotionList[0]) / globalCount
    ratioList[1] = float(globalEmotionList[1]) / globalCount
    ratioList[2] = float(globalEmotionList[2]) / globalCount
    print globalCount, ratioList
    pass

def updateGlobalCount(arg): #hacky workarounds to get tweet total up a scope
    global globalTweetTotal
    globalTweetTotal = arg


def calcRollingTotal(): #calculate rolling average
    global globalCount
    global lastCount
    global globalTweetTotal
    global globalEmotionList
    globalCount = globalTweetTotal - lastCount
    lastCount = globalTweetTotal
    globalEmotionList[0] = 0 #reset emotion list when you do
    globalEmotionList[1] = 0
    globalEmotionList[2] = 0
    pass

def updateGlobalList(arg):
    global globalEmotionList
    globalEmotionList = arg
    pass

class listener(StreamListener):
    tweetTotal = 0
    emotionList = [0,0,0]

    def reset(arg):
        pass

    def on_status(self, data):
        j = data._json
        if j['lang'] == 'en':
            tweetData = tc.stripPunctuation(data.text)
            emotion =  classifierInstance.classify(classifierObj.extract_features(tweetData.split()))
            self.tweetTotal += 1
            self.emotionList = adjustList(emotion, self.emotionList)
            updateGlobalCount(self.tweetTotal)
            updateGlobalList(self.emotionList)
            calculateRatio()
        return(True)

    def on_error(self, status):
        if status == 401:
            print "make sure VM and host clock are in sync"
        else:
            print status


oauth = austin_oauth.getOAuth()

classifierInstance = classifierObj.getClassifier()

streamInstance = Stream(oauth, listener()) #sets up listener


def startStream(search):
    print search

    if search == "":
        streamInstance.sample(async=True) #if empty, get sample of twitter

        pass
    else:
        streamInstance.filter(track=[search],async=True) #otherwise search for that query
    pass


def stopStream():
    streamInstance.disconnect()
    pass

#musicianStream.disconnect() to close stream
