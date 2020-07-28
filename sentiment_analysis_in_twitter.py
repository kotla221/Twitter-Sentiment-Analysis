# -*- coding: utf-8 -*-
"""Sentiment Analysis in Twitter

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17xafDm7uyiXVTmtWJcjumB8X8TUAWb9G
"""

#Import the tweepy package for accessing Twitter APIs in Python
import tweepy
#Import textblob package for sentiment anaysis of each tweet fetched from the API
from textblob import TextBlob
import matplotlib.pyplot as plt
def percentage(part,whole):
    return 100 * float(part) / float(whole)
#API Keys required for supporting the usage of the Twitter APIs
#Access and Consumer keys and secret for authenticating this script to work with the Twitter API
consumerKey = '9oyfw8phVoKtKl6QRWRhPAIxP'   #give your values here
consumerSecret = 'oOjSoKvWYRtUIoGZa7tt3ySoVJj5UQNxJ2Txc1FCWJS2LHsa5y'
accessToken = '920163998523203586-YlL0u7LHhOcw0qBrlDuFtVSXKFki6uB'
accessTokenSecret = 'VOz1TINUYQFRSGJnMdZxMBY0Y265VaAYfAbiUu0P10MJ4'

#Authenticating with Twitter for using its API provided he above keys
auth=tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)

#API variable for communicating our actions to the Twitter APIs
api=tweepy.API(auth)
#Asking the topic from the tweet_use
searchTerm=input("Enter keyword/tag to search about:")
NoOfTerms=int(input("Enter how many tweets you want to search"))

tweets=tweepy.Cursor(api.search,q=searchTerm).items(NoOfTerms)

positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    if(analysis.sentiment.polarity == 0):
        neutral +=1
    elif(analysis.sentiment.polarity <0.00):
        negative +=1
    elif(analysis.sentiment.polarity >0.00):
        positive +=1
    
positive = percentage(positive,NoOfTerms)
negative =percentage(negative,NoOfTerms)
neutral = percentage(neutral,NoOfTerms)
polarity =percentage(polarity,NoOfTerms)

positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')
print("How many people are reacting on" +searchTerm+"by analyzing"+str(NoOfTerms ) +"Tweets")
if(polarity==0):
    print("neutral")
elif(polarity<0.00):
    print("negative")
elif(polarity>0.00):
    print("positive")
    
labels = ['Positive[' +str(positive)+'%]','Negative[' +str(negative) +'%]','Neutral[' +str(neutral)+'%]']
                    
sizes=[positive,negative,neutral]
colors=['yellow','blue','red']
patches,text=plt.pie(sizes,colors=colors,startangle=45)
plt.legend(patches,labels,loc="best")
plt.title("Tweet Analysis"+searchTerm+"with the "+str(NoOfTerms))
plt.axis('equal')
plt.show()