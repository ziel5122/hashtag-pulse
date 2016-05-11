from pymongo import MongoClient
import random
import nltk
import re
import string
import csv

word_features = []

class TweetClassifier:
    def __init__(self):
        '''
        tweets = []
        with open("/home/austin/CST205/hashtag-pulse/data/training.1600000.processed.noemoticon.csv", 'rb') as file:
            reader = csv.reader(file)
            for row in reader:
                item = []
                tweet_text = strip_punctuation(row[5])
                item.append([word.lower() for word in tweet_text.split() if (len(word) >= 3 and re.search('[0-9]', word) == None)])
                item.append(row[0])
                tweets.append(item)
        
        print "done reading"
        self.word_features = get_word_features(get_words_in_tweets(tweets))
        
        training_set = nltk.classify.apply_features(self.extract_features, tweets, True)
        #print training_set[0][0]
        self.classifier = nltk.NaiveBayesClassifier.train(training_set)
        print "done training"
        self.classifier.show_most_informative_features(10)
        #self.classifier = nltk.NaiveBayesClassifier.train(tweets)
        '''
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
        print tweet
        return self.classifier.classify(self.extract_features(tweet))
      
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

def strip_punctuation(text):
    return re.sub('[^0-9a-zA-Z\']', ' ', text)
