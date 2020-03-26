
# twittoff/twitter_services.py

import os
from dotenv import load_dotenv
import tweepy
from pprint import pprint

load_dotenv()

consumer_key = os.getenv("TWITTER_API_KEY", default="OOPS")
consumer_secret = os.getenv("TWITTER_API_SECRET", default="OOPS")
access_token = os.getenv("TWITTER_ACCESS_TOKEN", default="OOPS")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", default="OOPS")

def twitter_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print("AUTH", type(auth))
    api = tweepy.API(auth)
    print("API", type(api)) #> <class 'tweepy.api.API'>
    return api


if __name__ == "__main__":
    
    api = twitter_api()
    screen_name = 'austen'
    print('-----')
    print('USER...')

    user = api.get_user(screen_name)
    print(type(user))
    print(user.screen_name)
    print(user.followers_count)
    pprint(user._json)

    print('--------')
    print('STATUSES')

    statuses = api.user_timeline(screen_name, tweet_mode='extended', count=5, exclude_replies=True, include_rt=False)
    for status in statuses:
        print(type(status))
        pprint(status._json)
        print(status.full_text)
