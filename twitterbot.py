import os
from twitter import *


class Bot(Api):
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        super().__init__(consumer_key, consumer_secret, access_token_key, access_token_secret)
        self.PostUpdate("teste")


access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']
twitter_key = os.environ['TWITTER_KEY']
twitter_secret = os.environ['TWITTER_SECRET']

api = Bot(consumer_key=twitter_key,
                      consumer_secret=twitter_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)


