import tweepy
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

toReply = "chahrazzzz" #user to get most recent tweet
api = tweepy.API(auth)

#get the most recent tweet from the user
tweets = api.user_timeline(screen_name = toReply, count=1)

for tweet in tweets:
    api.update_status("@" + toReply + " aaaa", in_reply_to_status_id = tweet.id)

