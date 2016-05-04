from pymongo import MongoClient
import random
import nltk

binary = False

client = MongoClient('argon.plttn.me', 27017)
db = client['hashtag-pulse']
db.authenticate('pulseUser', '+xCh4VduYDX1cG')

cursor = db.tweets.find({'$or':[{'label':"happy/excited"},{'label':"joke"},{'label':"sad/disappointed"},{'label':"angry"}]},{'text':1,'label':1,'_id':0})

tweets = []

count = 0
for tweet in cursor:
    item = []
    item.append([word.lower() for word in tweet['text'].split() if len(word) >= 3])
    if binary:
        if (tweet['label'] == 1 or tweet['label'] == 2):
            item.append(1)
        else:
            item.append(3)
    else:
        item.append(tweet['label'])
    tweets.append(item)
    count += 1

print len(tweets)
print count

print tweets[0:15]

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

word_features = get_word_features(get_words_in_tweets(tweets))
print word_features[0]

training_set = nltk.classify.apply_features(extract_features, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)

num_right = 0
for i in range(0, len(tweets)):
    predicted = classifier.classify(extract_features(tweets[i][0]))
    actual = tweets[i][1]
    if predicted == actual:
        num_right += 1

print float(num_right) / len(tweets)

classifier.show_most_informative_features(10)

#tweets[i] is a piece of data
#tweets[i][0] is a list of tokens
#tweets[i][1] is the label

'''
while (cursor.hasNext()):
    tweet = cursor.next()
    print tweet['text']

    .split("\"")[1]
'''
