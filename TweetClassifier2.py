from pymongo import MongoClient
import random
import nltk
import re
import string
import csv

word_features = []

class TweetClassifier:
    def __init__(self):
        print "a"
        
    def getClassifier(self):
        return self.classifier
        
    def setClassifier(self, classifier):
        self.classifier = classifier    
        
    def extract_features(self, document):
        document_words = set(document)
        features = {}
        for word in self.word_features:
            features[word] = (word in document_words)
        return features
    
    def set_word_features(self, wordlist):
        wordlist = nltk.FreqDist(wordlist)
        self.word_features = wordlist.keys()
        
    def classify(self, tweet):
        num = self.classifier.classify(self.extract_features(tweet))
        print num
        return num
      
    def extract_features(self, document):
        document_words = set(document)
        features = {}
        for word in self.word_features:
            features[word] = (word in document_words)
        return features
      
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in self.word_features:
        features[word] = (word in document_words)
    return features
        
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features
        
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def stripPunctuation(text):
    return re.compile('[^a-zA-Z0-9\']').split(text)
    #return re.sub('[^a-zA-Z0-9\']', ' ', text)
