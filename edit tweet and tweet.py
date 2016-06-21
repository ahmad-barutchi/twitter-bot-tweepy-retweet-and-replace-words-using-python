#!/usr/bin/env python
# encoding: utf-8
i=0
e=0
import tweepy, time
import tweepy.error

print("1")

CONSUMER_KEY = ''#Required
CONSUMER_SECRET = ''#Required
ACCESS_KEY = ''#Required
ACCESS_SECRET = ''#Required

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print("2")
for tweet in tweepy.Cursor(api.search, q="Syria", count=300, result_type="recent").items(): #Edit the word Syria Only
    try:
        print(tweet.created_at, tweet.text)
        print(tweet.text)
        list1 = (tweet.text)
        list2 = (tweet.text)

        newlist = newlist.replace("war in Syria", "peace in World")
        #Edit the first bracket for the word you want to change from the tweet in the new one in the second bracket
 
        list2 = (tweet.text)
        print("3")
        if not newlist == list2:
            print(newlist)
            i = + 1
            print("################")
            print("new tweet", i)
            api.update_status(status=newlist)
            time.sleep(99)

    except tweepy.error.TweepError:
        e=+1
        print("### error happend: but dosent matter ###", e)

    print("4")
    time.sleep(1)

time.sleep(1)
print("finish")