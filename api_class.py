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
        self.iex_api_id = os.getenv('IEX_SECRET_TKN')
        self.twitter_api_id = os.getenv('TWITTER_SECRET_KEY, TWITTER_KEY')
        self.api_key = os.getenv('GLASSNODE_KEY')
        self.glassnode_api_url='https://api.glassnode.com/v1/metrics/'
    


    def get_supply(self,symbols,duration=sd.Current,from_date='',to_date='',frequency_interval='24h'):
        supply_endpoint='current'
        if duration==sd.Current:
            supply_endpoint='current'
        if duration==sd.Active_1d_1w:
            supply_endpoint='active_1d_1w'
        if duration==sd.Active_1Y_2Y:
            supply_endpoint='active_1y_2y'
        if duration==sd.Active_24h:
            supply_endpoint='active_24h'
        if duration==sd.Active_2Y_3Y:
            supply_endpoint='active_2y_3y'
        if duration==sd.Active_More_5Y:
            supply_endpoint='active_more_5y'
        
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
        return df

    def get_Transactions(self,symbols,transactiontype=tt.TransfersVolumeSum,from_date='',to_date='',frequency_interval='24h'):
        transcation_endpoint='transfers_volume_sum'
        if transactiontype==tt.TransfersVolumeSum:
            transcation_endpoint='transfers_volume_sum'
        if transactiontype==tt.TransfersVolumeAdjustedMean:
            transcation_endpoint='transfers_volume_adjusted_mean'
        if transactiontype==tt.TransfersVolumeAdjustedMedian:
            transcation_endpoint='transfers_volume_adjusted_median'
        if transactiontype==tt.TransfersVolumeAdjustedSum:
            transcation_endpoint='transfers_volume_adjusted_sum'
        if transactiontype==tt.TransfersVolumeMean:
            transcation_endpoint='transfers_volume_mean'
        if transactiontype==tt.TransfersVolumeMedian:
            transcation_endpoint='transfers_volume_median'
        
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
        return df
    
    # Fetch 
    def get_addresses(self,symbols,addresstype=adtype.Min_10k_Count,from_date='',to_date='',frequency_interval='24h'):
        address_endpoint='transfers_volume_sum'
        if addresstype==adtype.Min_10k_Count:
            address_endpoint='min_10k_count'
        if addresstype==adtype.Min_Point_1_Count:
            address_endpoint='min_point_1_count'
        if addresstype==adtype.Non_Zero_Count:
            address_endpoint='non_zero_count'
        
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
        return df

    def convert_to_datetime(self,unix_timestamp):
        return datetime.fromtimestamp(unix_timestamp)
