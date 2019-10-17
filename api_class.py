import pandas as pd
import os
import numpy
import requests
import json 
#import tweepy
from datetime import datetime
from transactions_type import transactions_type as tt
from supply_enum import supply_duration as sd
from address_type import address_type as adtype

class apiservice:
    #declaring global variables 
    iex_api_id = None
    twitter_api_id = None
    glassnode_api_url = None
    api_key=''
    

    #calling the APIs
    def __init__(self):
       self.assign_variables()

    def get_supply(self,symbols,duration=sd.Current,from_date='',to_date='',frequency_interval='24h'):
        supply_endpoint=f'{duration.name.lower()}'
        self.glassnode_api_url+=f'supply/{supply_endpoint}?api_key={self.api_key}'

        if from_date!='' and to_date !='':
            from_date_unix=datetime.timestamp(pd.to_datetime(from_date))
            to_date_unix=datetime.timestamp(pd.to_datetime(to_date))
            self.glassnode_api_url+=f'&a={symbols}&s={from_date_unix}&u={to_date_unix}&i={frequency_interval}'
        else:
            self.glassnode_api_url+=f'&a={symbols}&i={frequency_interval}'
        
        supply_data=requests.get(self.glassnode_api_url).content
        df=pd.read_json(supply_data,orient='records')
        df.rename(columns={'t':'DateTime','v':'Amount'},inplace=True)
        df['DateTime']=df.apply(lambda x: self.convert_to_datetime(x['DateTime']),axis=1)
        self.assign_variables()
        return df

    def get_Transactions(self,symbols,transactiontype=tt.Transfers_Volume_Sum,from_date='',to_date='',frequency_interval='24h'):
        transcation_endpoint=f'{transactiontype.name.lower()}'
        self.glassnode_api_url+=f'transactions/{transcation_endpoint}?api_key={self.api_key}'

        if from_date!='' and to_date !='':
            from_date_unix=datetime.timestamp(pd.to_datetime(from_date))
            to_date_unix=datetime.timestamp(pd.to_datetime(to_date))
            self.glassnode_api_url+=f'&a={symbols}&s={from_date_unix}&u={to_date_unix}&i={frequency_interval}'
        else:
            self.glassnode_api_url+=f'&a={symbols}&i={frequency_interval}'
        
        transaction_data=requests.get(self.glassnode_api_url).content
        df=pd.read_json(transaction_data,orient='records')
        df.rename(columns={'t':'DateTime','v':'Amount'},inplace=True)
        df['DateTime']=df.apply(lambda x: self.convert_to_datetime(x['DateTime']),axis=1)
        self.assign_variables()
        return df

    def get_addresses(self,symbols,addresstype=adtype.Min_10k_Count,from_date='',to_date='',frequency_interval='24h'):
        address_endpoint=f'{addresstype.name.lower()}'
        self.glassnode_api_url+=f'addresses/{address_endpoint}?api_key={self.api_key}'

        if from_date!='' and to_date !='':
            from_date_unix=datetime.timestamp(pd.to_datetime(from_date))
            to_date_unix=datetime.timestamp(pd.to_datetime(to_date))
            self.glassnode_api_url+=f'&a={symbols}&s={from_date_unix}&u={to_date_unix}&i={frequency_interval}'
        else:
            self.glassnode_api_url+=f'&a={symbols}&i={frequency_interval}'
        
        address_data=requests.get(self.glassnode_api_url).content
        df=pd.read_json(address_data,orient='records')
        df.rename(columns={'t':'DateTime','v':'Amount'},inplace=True)
        df['DateTime']=df.apply(lambda x: self.convert_to_datetime(x['DateTime']),axis=1)
        self.assign_variables()
        return df

    def convert_to_datetime(self,unix_timestamp):
        return datetime.fromtimestamp(unix_timestamp)

    def assign_variables(self):
        self.iex_api_id = os.getenv('IEX_SECRET_TKN')
        self.twitter_api_id = os.getenv('TWITTER_SECRET_KEY, TWITTER_KEY')
        self.api_key = os.getenv('GLASSNODE_KEY')
        self.glassnode_api_url='https://api.glassnode.com/v1/metrics/'
