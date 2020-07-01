from decouple import config
import tweepy

consumer_key = config('TWIT_KEY')
consumer_secret = config('TWIT_SECRET_KEY')
access_token = config('TWIT_ACCESS_TOKEN')
access_token_secret = config('TWIT_ACCESS_TOKEN_SECRET')

Auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
Auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(Auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
