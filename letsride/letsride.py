import tweepy

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '1234abcd...'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '1234abcd...'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1234abcd...'#keep the quotes, replace this with your access token
ACCESS_SECRET = '1234abcd...'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)