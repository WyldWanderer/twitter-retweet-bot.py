#First step is to apply for developer status with Twitter through developer.twitter.com and generate API keys
import tweepy

#Copy API keys from developer profile and add to code below
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Put each user you want to pull the most recent tweet from in the user_name list in the format '@UserName'seperated by commas
user_name = []
tweetList = []
oldTweets = []

#Code to create list of tweets from designated users, making sure none have be retweeted before
def getTweet (user_name):
    for users in user_name:
        user = api.get_user(users)
        tweetInfo = user._json.get('status')
        tweetId = tweetInfo.get('id')
        if tweetId not in oldTweets:
            tweetList.append(tweetId)

#Code to take all tweets in generated list and retweet             
def retweets (tweetList):
    for tweet in tweetList:
        api.retweet(tweet)
        oldTweets.append(tweet)
    tweetList.clear()
    return oldTweets

#Run program functions and return message when successful
getTweet(user_name)
retweets(tweetList)
print ('Successful Run')

        
        



