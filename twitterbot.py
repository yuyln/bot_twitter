import os
from twitter import *

access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']
twitter_key = os.environ['TWITTER_KEY']
twitter_secret = os.environ['TWITTER_SECRET']
api = Api(consumer_key=twitter_key,
                      consumer_secret=twitter_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)

#print(api.VerifyCredentials())
for i in range(100):
    print(api.PostDirectMessage(str(i), '3337775116', return_json=True))
