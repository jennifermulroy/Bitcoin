import pandas as pd
import os
import numpy
import requests
import json 
import tweepy

#declaring global variables 
class data_collection:
    iex_api_id = None
    twitter_api_id = None
    coincap_url = None
    glass_node_api = None
    coin_market_cap_api = None
    nomics_api = None
    coin_api = None 


#calling the APIs
    def __init__(self):
        iex_api_id = os.getenv('IEX_SECRET_TKN')
        twitter_api_id = os.getenv('TWITTER_SECRET_KEY, TWITTER_KEY')
        coincap_url = "http://api.coincap.io/v2"
        glass_node_api = os.getenv('GLASSNODE_KEY')
        coin_market_cap_api = os.getenv('COIN_MARKETCAP_KEY')
        nomics_api = os.geten('NOMICS_KEY')
        coin_api = os.getevn("COIN_API_KEY")

    def getiex(self):
        iex_data = requests.get(iex_api_id)

    def gettwitter(self):
        twitter_data = requests.get(twitter_api_id)

    def getcoincap(self)
        coincap = requests.get(coincap_url)

    def getglassnode(self):
        glassnode_data = requests.get(glass_node_api)

    def getcoinmarketcap(self):
        coinmarketcap_data = requests.get(coin_market_cap_api) 

    def getnomics(self:)
        nomics_data = requests.get(nomics_api)

    def getcoinapi(self):
        coin_data = requests.get(coin_api)
    

        