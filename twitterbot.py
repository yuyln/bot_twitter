import os
from twitter import *
import rule34
from time import sleep
from random import choice
import datetime


class Bot(Api):
	hentais = ['darkness_(konosuba)',
			   'tristana',
			   'vayne']
	def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret, sleep_on_rate_limit=False):
		super().__init__(consumer_key, consumer_secret, access_token_key, access_token_secret, sleep_on_rate_limit)
		print("O bot ligou")
	
	def posta_rule(self):
		r34 = rule34.Sync()
		img = r34.getImages(choice(Bot.hentais))
		try:
			img = choice(r34.getImages(choice(Bot.hentais)))
			img1 = img.file_url
			img = r34.download(img.file_url)
			self.PostUpdate(status="", media=img)
			os.remove(img)
			with open('log.txt', 'a') as arq:
				arq.write(f'Postado: {img1}\nData:{datetime.datetime.now().strftime("%H:%M:%S - %d/%m/%Y")}\n---------------------------\n')		
		except Exception as e:
			with open('log.txt', 'a') as arq:
				arq.write(f'Erro: {e}\nData:{datetime.datetime.now().strftime("%H:%M:%S - %d/%m/%Y")}\n---------------------------\n')
				

access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']
twitter_key = os.environ['TWITTER_KEY']
twitter_secret = os.environ['TWITTER_SECRET']

api = Bot(consumer_key=twitter_key,
                      consumer_secret=twitter_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)
                      
api.posta_rule()
