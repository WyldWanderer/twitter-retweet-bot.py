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

#Code to create list of tweets from designated users
def getTweet (user_name):
    for users in user_name:
        user = api.get_user(users)
        tweetInfo = user._json.get('status')
        tweetId = tweetInfo.get('id')
        tweetList.append(tweetId)

#checks list of tweets agains list of tweets already retweeted, reads from .txt file set up separately
def scrubList (tweetList):
    with open('old_tweets.txt', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            oldTweets.append(int(currentPlace))
        for tweet in tweetList:
            if tweet in oldTweets:
                tweetList.remove(tweet)
    return tweetList
    return oldTweets

#Takes all tweets in scrubbed list and retweets
def retweets (tweetList):
    scrubList(tweetList)
    for tweet in tweetList:
        if tweet not in oldTweets:
            api.retweet(tweet)
            oldTweets.append(tweet)
    return oldTweets

#writes ID's of used tweets to .txt file for reference by scrubList
def saveOldTweets (oldTweets):
    with open('old_tweets.txt', 'w') as filehandle:
        for tweet in oldTweets:
            filehandle.write('%s\n' % tweet)


#Run program functions and return message when successful
getTweet(user_name)
retweets(tweetList)
saveOldTweets(oldTweets)
print ('Successful Run')
