import cPickle
import TweetClassifier2 as tc
import nltk
import csv
import re
import random

clf_file = open('160000.pickle','wb')
word_features = []

classifier = tc.TweetClassifier()
tweets = []
with open("/home/austin/CST205/data/training.1600000.processed.noemoticon.csv",'rb') as file:
    reader = csv.reader(file)
    for row in reader:
        if random.randint(1,10) == 1:
            item = []
            tweet_text = tc.strip_punctuation(row[5])
            item.append([word.lower() for word in tweet_text.split() if (len(word) >= 3 and re.search('[0-9]', word) == None)])
            item.append(row[0])
            tweets.append(item)
        
    print "done reading"
    classifier.set_word_features(tc.get_words_in_tweets(tweets))
    print "word features set"
    training_set = nltk.classify.apply_features(classifier.extract_features,tweets,True)
    print training_set[0]
    classifier.setClassifier(nltk.NaiveBayesClassifier.train(training_set))
    print "done training"
    classifier.getClassifier().show_most_informative_features(10)
    cPickle.dump(classifier, clf_file)
    clf_file.close()

