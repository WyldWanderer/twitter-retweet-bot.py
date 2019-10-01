import tweepy

CONSUMER_KEY = 'FIUXbox6Xen79Qhx29FUfkiB2'
CONSUMER_SECRET = 'bgpxM3j8efnXpuo5q24DAjX4OInSpMGwvNF8SOzG1V7tYjNNuN'
ACCESS_KEY = '1155300186362482690-SarBJ3IG3IaLLzAQd3Am5AzSbj9vjP'
ACCESS_SECRET = 'pfSWZ8qGQOyKc4wd1ScbapfkVS0U8EsH3ONRmdeuFXJ2b'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#put each user you want to pull the most recent tweet from in the user_name list in the format '@UserName'
user_name = []
tweetList = []
oldTweets = []

def getTweet (user_name):
    for users in user_name:
        user = api.get_user(users)
        tweetInfo = user._json.get('status')
        tweetId = tweetInfo.get('id')
        tweetList.append(tweetId)

def retweets (tweetList):
    for tweet in tweetList:
        if tweet not in oldTweets:
            api.retweet(tweet)
            oldTweets.append(tweet)
    tweetList.clear()        
           
getTweet(user_name)
retweets(tweetList)


        
        



