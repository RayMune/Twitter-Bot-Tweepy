import tweepy 
import requests
import time

consumer_key='EzGEOiu'
consumer_secret='SURsP86'
access_token='15886284'
access_token_secret='Hj0gA3k1'

#Authentication to twitter
auth = tweepy.OAuthHandler('consumer_key','consumer_secret')
authenticator.set_access_token('access_token','access_token_secret')

#creating api object and setting authentication handler
api=tweepy.API(auth, wait_on_rate_limit='true')

#Following another user
api.create_friendship(screen_name='BarackObama')

#creating a post
api.update_status("Hey, Happy new month, We can confirm some of our product users are experiencing difficulties due to software maintenance.")

#fetching mentions
mentions = api.mentions_timeline()

#replying to each mention
for mention in mentions:
#check if the mention contains a keyword
    if mention.text.find("complain") != -1:
        #reply to the mention
        api.update_status("Hi, I saw your mention! Here is my reply: " % (mention.user.screen_name, "we are currently working to restore your connection online"))

#Analyzing Tweet sentiments 

#fetch tweets
tweets = api.search(q="Ukweli logistics")

#analyze a single tweet
for tweet in tweets:
    # Get the text of the tweet
    text = tweet.text

    #get the sentiment of the tweet
    sentiment = get_sentiment(text)

    #print the tweet and its sentiment
    print("Tweet:", text)
    print("Sentiment:", sentiment)

#Analyze multiple tweets

#search for tweets containing the word "python"
tweets = api.search(q="ukweli logistics ", count=100)

#create a DataFrame to store the tweets
df = pd.DataFrame(tweets)

#print the first few rows of the DataFrame
print(df.head())

#analyze the sentiment of the tweets
from textblob import TextBlob

#create a function to calculate the sentiment of a tweet
def sentiment(tweet):
    #create a TextBlob object from the tweet text
    analysis = TextBlob(tweet.text)

    #get the polarity of the tweet
    polarity = analysis.sentiment.polarity

    #return the polarity
    return polarity

#calculate the sentiment of each tweet
df["sentiment"] = df["text"].apply(sentiment)

#print the sentiment of the first few tweets
print(df["sentiment"].head())
