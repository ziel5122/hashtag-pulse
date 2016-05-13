import TweetClassifier2 as tc
import cPickle
from tweepy.streaming import StreamListener
from tweepy import Stream

'''
import austin_oauth
import json
from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
import TweetClassifier2 as tc
import csv
import re
import cPickle
'''

class TweetStream(StreamListener):
    def build(self):
        clf_file = open('tweet_classifier_small.pickle','rb')
        self.classifier = cPickle.load(clf_file)
        print self.classifier.getClassifier().classify(self.classifier.extract_features(['first', 'assesment', 'the', 'fucking', 'rocks']))
        clf_file.close()
        
        self.emotion_total = {'0':0,'2':0,'4':0}
        self.total_tweets = 0
        self.emotions_per = {'0':0,'2':0,'4':0}
        self.tweets_per = 0

    def on_status(self, data):
        tweet = data._json
        if tweet['lang'] == 'en':
            tweet_text = tc.stripPunctuation(tweet['text'])
            self.updateCounts(self.classifier.getClassifier().classify(self.classifier.extract_features(tweet_text.split())))

    def updateCounts(self, emotion):
        self.updateTotal(emotion)
        self.updateCountsPer(emotion)
        
    def updateTotal(self, emotion):
        self.emotion_total[emotion] += 1
        self.total_tweets += 1
       
    def updateCountsPer(self, emotion):
        self.emotions_per[emotion] += 1
        self.tweets_per += 1
        
    def getRate(self):
        if self.tweets_per == 0:
            return [0,0,0]
        else:
            rates = map(lambda x: float(self.emotions_per[x]) / self.tweets_per, self.emotions_per)
            self.tweets_per = 0
            self.emotions_per = dict.fromkeys(self.emotions_per, 0)
            return rates
            
    def getTotal(self):
        if self.total_tweets == 0:
            return [0,0,0]
        else:
            ratios = []
            for key in self.emotion_total:
                ratios.append(float(self.emotion_total[key]) / self.total_tweets)
            return ratios
        
    def on_error(self, status):
        if status == 401:
            print "make sure VM and host clock are in sync"
        else:
            print status
            
    def reset(self):
        self.total_tweets = 0
        self.tweets_per = 0
        self.emotions_per = dict.fromkeys(self.emotions_per, 0)
        self.emotion_total = dict.fromkeys(self.emotion_total, 0)
        
