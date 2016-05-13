import TweetClassifier2 as tc
import csv
import re
import cPickle
import random

clf_file = open('16000.pickle','rb')
classifier = cPickle.load(clf_file)
clf_file.close()
#classifier = TweetClassifier2.TweetClassifier()

tweets = []
with open("/home/austin/CST205/data/testdata.manual.2009.06.14.csv", 'rb') as file:
    reader = csv.reader(file)
    counter = 0
    for row in reader:
        item = []
        tweet_text = tc.stripPunctuation(row[5])
        item.append([word.lower() for word in tweet_text.split() if (len(word) >= 3 and re.search('[0-9]', word) == None)])
        item.append(row[0])
        tweets.append(item)
        counter += 1
        print counter
 
num_right = 0       
for tweet in tweets:
    result = classifier.getClassifier().classify(classifier.extract_features(tweet[0]))
    print tweet[0]
    print result
    if result == tweet[1]:
        num_right = num_right + 1

print float(num_right) / len(tweets)
