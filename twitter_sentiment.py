#import the Dependencies

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob

#Api key To connect to Twitter

consumer_key='DrOmrmvYIpbOJjAPXhVq5FK0I'
consumer_secret='Oo4jjoQybkwmsHxqJxS30T8xbtA7cd48h8ZduaLzkfNJcUnN9Q'

access_token='525127766-JGqY6cyW8APO7JEXmtI12rAHgNDZCMjThlsuq82P'
access_token_secret='Tea7niVAHRFtV9Uiq9gnNsuIwSjPOj724nI1ouP4VCBsf'

#Passing the Value of Api key

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#calling Dependencies 

api=tweepy.API(auth)

#Searching the sentence related to the given word

public_tweets=api.search('Trump')

#looping in the sentence  and analysing the sentiment ranges from -1 to 1

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)