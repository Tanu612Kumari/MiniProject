"""
Name : Tanu Kumari
Branch : IT
University roll no.: 2013755
"""

import tweepy                     #this python package gives us a way to access twitter API with python
import re                         #this library is used for regular expressions
from  textblob import TextBlob    #TextBlob is a python library for processing textual data
import matplotlib.pyplot as plot  #This library is used for ploting graphs

#following function is used to remove unwanted data from the tweeter data
def clean_data(tweet):
		return " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

#Following function is used to calculate the percentage of tweeter data based on polarity
def percentage(x,y):
    return 100*(float(x)/float(y)) 

# Following are the four access keys and token we get from tweeter to use tweeter API 
consumer_key = "8AO6OU5ubyi4XO47b1C7Sjdlz"
consumer_secret = "FS1usPrfPolvjLXbwGka5N8TWkOZhUsdxGmmTwuO016koesUSt"
access_token = "1151573806680592384-OUFeUtpsRFZM6jQxl1AG99NEjlY0Kt"
access_token_secret = "KKHmkHkDGVaDof8XK4fKKI52DmNl4vZlaXnx85WRfd4Lr"

#following three line are used to conenet the jump server after that web server and finally API server of tweeter
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)


tweet_data=api.search('Cricket',count=100)

fout=open('tweets.txt','w')
for i in tweet_data:
  fout.write(i.text)
  fout.write("\n")
fout.close()


fout=open('data.txt','w')
for i in tweet_data:
  data=clean_data(i.text)
  fout.write(data)
  fout.write("\n")
fout.close()

positive_tweets=0
negative_tweets=0
neutral_tweets=0
List_of_pos_tweets=[]
List_of_neg_tweets=[]
List_of_neu_tweets=[]


for tweet in tweet_data:
   analysis=TextBlob(clean_data(tweet.text))

   print(analysis)
   p=analysis.sentiment.polarity 
   if p > 0:
      print("\nPolarity = positive\n\n")
      positive_tweets=positive_tweets+1
      List_of_pos_tweets.append(tweet.text)
   elif p == 0 :
      print("\nPolarity = neutral\n\n")
      neutral_tweets=neutral_tweets+1
      List_of_neu_tweets.append(tweet.text)
   else :
      print("\nPolarity = negative\n\n")
      negative_tweets=negative_tweets+1
      List_of_neg_tweets.append(tweet.text)


positive_tweets=percentage(positive_tweets,count)
negative_tweets=percentage(negative_tweets,count)
neutral_tweets=percentage(neutral_tweets,count)

positive_tweets=format(positive_tweets,'.2f')
negative_tweets=format(negative_tweets,'.2f')
neutral_tweets=format(neutral_tweets,'.2f')
print('\nPercentage of positive tweets are ',positive_tweets)
print('\nPercentage of negative tweets are ',negative_tweets)
print('\nPercentage of neutral tweets are ',neutral_tweets)

# ploting pieChart
plot.title('Pie Chart of the result of Sentiment Analysis')
plot.pie([positive_tweets,negative_tweets,neutral_tweets],labels=['positive','negative','neutral'],colors=['lime','pink','yellow'],autopct="%1.1f%%",shadow=True)
plot.show()