from pymongo import MongoClient
import random

client = MongoClient('argon.plttn.me', 27017)
db = client['hashtag-pulse']
db.authenticate('pulseUser', '+xCh4VduYDX1cG')

num_records = db.tweets.count()

exit = False
while (not exit):
    number = random.randint(0,num_records)
    record = db.tweets.find({'label':{'$exists':False}}).limit(-1).skip(number).next()
    #record = db.tweets.find_one({'label':{'$exists':False}})
    print "\n" + str(record['_id']) + "\n" + record['text']
    print("")
    print("Choose a label: \n\t1=happy/excited  2=joke  3=sad/disappointed  4=angry  5=ad\n\t9=skip 0=quit")
    response = input("enter a number: ")
    exit = {
        1:lambda response:not db.tweets.update_one(
                {'_id':record['_id']},{'$set':{'label':response}}
            ),
        2:lambda response:not db.tweets.update_one(
                {'_id':record['_id']},{'$set':{'label':response}}
            ),
        3:lambda response:not db.tweets.update_one(
                {'_id':record['_id']},{'$set':{'label':response}}
            ),
        4:lambda response:not db.tweets.update_one(
                {'_id':record['_id']},{'$set':{'label':response}}
            ),
        5:lambda response:not db.tweets.update_one(
                {'_id':record['_id']},{'$set':{'label':response}}
            ),
        9:lambda response:not db.tweets.update_one(
                {'_id':record['_id']},{'$set':{'label':0}}
            ),
        0:lambda response:True
    }[response](response)
