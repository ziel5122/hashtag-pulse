from pymongo import MongoClient
import random
import nltk

class TweetClassifier:
    def __init__(self, binary):
        db = self.getMongo()
        cursor = db.tweets.find({'$or':[{'label':"happy/excited"},{'label':"joke"},{'label':"sad/disappointed"},{'label':"angry"}]},{'text':1,'label':1,'_id':0})
        
        tweets = []
        for tweet in cursor:
            item = []
            item.append([word.lower() for word in tweet['text'].split() if len(word) >= 3])
            if binary:
                if (tweet['label'] == 'happy/excited' or tweet['label'] == 'joke'):
                    item.append('happy/excited')
                else:
                    item.append('sad/disappointed')
            else:
                item.append(tweet['label'])
            tweets.append(item)
        
        self.word_features = self.get_word_features(self.get_words_in_tweets(tweets))
        
        training_set = nltk.classify.apply_features(self.extract_features, tweets)

        self.classifier = nltk.NaiveBayesClassifier.train(training_set)
   
    def getMongo(self):
        client = MongoClient('argon.plttn.me', 27017)
        db = client['hashtag-pulse']
        db.authenticate('pulseUser', '+xCh4VduYDX1cG')
        return db
    
    def extract_features(self, document):
        document_words = set(document)
        features = {}
        for word in self.word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features
        
    def classify(self, tweet):
        return self.classifier.classify(self.extract_features(tweet.split()))
        
    def get_word_features(self, wordlist):
        wordlist = nltk.FreqDist(wordlist)
        word_features = wordlist.keys()
        return word_features
        
    def get_words_in_tweets(self, tweets):
        all_words = []
        for (words, sentiment) in tweets:
            all_words.extend(words)
        return all_words

