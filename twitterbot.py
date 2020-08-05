import os
from twitter import *
import rule34
from time import sleep
from random import choice
import datetime


class Bot(Api):
        hentais = ['darkness_(konosuba)',
                   'tristana',
                   'vayne',
                   'hatsune_miku',
                   'asuka_langley_sohryu',
                   'aqua_(konosuba)',
                   'aqua_eyes',
                   'evangelion:_2.0_you_can_(not)_advance',
                   'megumin',
                   'kono_subarashii_sekai_ni_shukufuku_wo!',
                   'bikini',
                   'ahegao',
                   'asuna_(sao)',
                   'sword_art_online',
                   'paizuri',
                   'ahri',
                   'akali',
                   'anivia',
                   'ashe_(league_of_legends)',
                   'caitlyn',
                   'riot_games',
                   'diana',
                   'fiora',
                   'irelia',
                   'league_of_legends',
                   'jinx',
                   'raven',
                   'katarina',
                   'my_hero_academia',
                   'ochako_uraraka',
                   'kill_la_kill',
                   'eromanga_sensei',
                   'kirino_kosaka',
                   'dagashi_kashi',
                   'valorant',
                   'sage_(valorant)',
                   'jett_(valorant)',
                   'nekopara',
                   'kirigaya_suguha',
                   'nisekoi',
                   'kirisaki_chitoge',
                   'imouto_sae_ireba_ii',
                   'bunny_girl',
                   'seishun_buta_yarou_wa_bunny_girl_senpai_no_yume_wo_minai'
                   'ore_no_imouto_ga_konna_ni_kawaii_wake_ga_nai ',
                   'hinata_hyuuga']
        def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret, sleep_on_rate_limit=False):
                super().__init__(consumer_key, consumer_secret, access_token_key, access_token_secret, sleep_on_rate_limit)
                print("O bot ligou")
                print(Bot.hentais)
        def posta_rule(self):
                r34 = rule34.Sync()
                img = r34.getImages(choice(Bot.hentais))
                try:
                        cc = choice(Bot.hentais)
                        img = choice(r34.getImages(cc))
                        img1 = img.file_url
                        img = r34.download(img.file_url)
                        self.PostUpdate(status=f"Rule34 Search: {cc}\nURL: {img1}", media=img)
                        os.remove(img)
                        print(Bot.hentais)
                        print(f'Postado: {img1}\nData: {datetime.datetime.now().strftime("%H:%M:%S - %d/%m/%Y")}\n---------------------------\n')
                        with open('log.txt', 'a') as arq:
                                arq.write(f'Postado: {img1}\nData: {datetime.datetime.now().strftime("%H:%M:%S - %d/%m/%Y")}\n---------------------------\n')		
                except Exception as e:
                        print(Bot.hentais)
                        print(f'Erro: {e}\nData:{datetime.datetime.now().strftime("%H:%M:%S - %d/%m/%Y")}\n---------------------------\n')
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

while True:
	api.posta_rule()
	sleep(3600)
