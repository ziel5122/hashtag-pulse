from pymongo import MongoClient
import random
import nltk
from string import punctuation

binary = False

def strip_punctuation(s):
    return ''.join (c for c in s if c not in punctuation)
    pass


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def generate_classifier():
    client = MongoClient('argon.plttn.me', 27017)
    db = client['hashtag-pulse']
    db.authenticate('pulseUser', '+xCh4VduYDX1cG')


    cursor = db.tweets.find({'$or':[{'label':"happy/excited"},{'label':"joke"},{'label':"sad/disappointed"},{'label':"angry"}]},{'text':1,'label':1,'_id':0})

    tweets = []

    count = 0
    for tweet in cursor:
        item = []
        item.append([word.lower() for word in strip_punctuation(tweet['text']).split() if len(word) >= 3])
        if binary:
            if (tweet['label'] == 1 or tweet['label'] == 2):
                item.append(1)
            else:
                item.append(3)
        else:
            item.append(tweet['label'])
        tweets.append(item)
        count += 1

    word_features = get_word_features(get_words_in_tweets(tweets))

    training_set = nltk.classify.apply_features(extract_features, tweets)

    classifier = nltk.NaiveBayesClassifier.train(training_set)
    return classifier
    pass



# print float(num_right) / len(tweets)

def classify_tweet(tweet_text,classifierInstance): #need to tokenize tweet text
    print "did we get to classifier function?"
    item = []
    tweet_text = strip_punctuation(tweet_text)
    item.append([word.lower() for word in tweet_text.split() if len(word) >= 3])
    print classifierInstance.classify(extract_features(item)), tweet_text
    pass


#tweets[i] is a piece of data
#tweets[i][0] is a list of tokens
#tweets[i][1] is the label

'''
while (cursor.hasNext()):
    tweet = cursor.next()
    print tweet['text']

    .split("\"")[1]
'''
