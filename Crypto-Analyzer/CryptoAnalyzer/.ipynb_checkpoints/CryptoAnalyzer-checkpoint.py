import pandas as pd
import numpy as np
import pandas_datareader as pdr
from functools import reduce
from pathlib import Path

class GetPrices:
    
    def __init__(self):
        pass
    
    @classmethod
    def yahoo(cls,start_date="",end_date="",ticker_list=''):

        """ Gets yahoo price data for a given crypto/currency pair(ie.BTC-USD) within the 
        start and end date period. Returns a dictonary of dfs for each closing price.
        
        Args:
   
        date_start (datetime): starting date as MM-DD-YYYY format.
        date_end (datetime): ending date as MM-DD-YYYY format
        ticker: single or list of ticker/cypto-currency pair(BTC-USD)
        
        example: prices = Yahoo_Prices.get(start_date,end_date,['BTC-USD','ETH-USD','LTC-USD','AMD','YUM'])"""

        #Calls the api for each item in the asset list and create a list of Dataframe. 
        df_list = [pd.DataFrame(pdr.get_data_yahoo(i,start_date,end_date)['Close']).rename(columns={'Close':i}) for i in ticker_list]
        
        dataframe = reduce(lambda x, y: pd.merge(x, y, how='left',on='Date' ), df_list)
        
        return dataframe
    
    @classmethod
    def load_cvs_to_dataframe(self, sourcepath,indexcol='',dropcolumns=[]):
        csvfile=Path(sourcepath)
        _df=pd.read_csv(csvfile,infer_datetime_format=True,parse_dates=True)
        
        if indexcol!='' :
            _df.set_index(indexcol,inplace=True)

        if len(dropcolumns)!=0:
            _df.drop(columns=dropcolumns, inplace=True)
        return _df
    


class Stats:
    
    def __init__(self):
        pass
    
    @classmethod
    def beta(cls,tickers="",start_date="",end_date=""):
    
        """ Enter the Stock and Index in order"""
        beta_dict = {}
        
        if len(tickers) == 2:
            
            #get prices and returns
            prices = GetPrices.yahoo(start_date,end_date,tickers)
            returns = Stats.get_one(prices,'daily returns')

            covariance = returns.iloc[0:,0].cov(returns.iloc[0:,1])
            variance = returns.iloc[0:,0].var()
            beta = covariance / variance
            
            #append_dict
            beta_dict[f"{tickers[0]} variance"] = variance
            beta_dict[f"{tickers[0]} covariance"] = covariance
            beta_dict[f"{tickers[0]} beta"] = beta
            beta_dict["Index"] = tickers[1]

        else:
            beta_dict['No beta params passed'] = 'No beta params passed'
            
        dataframe = pd.DataFrame(beta_dict,index=[i for i in range(len(beta_dict.keys()))])
            
        return dataframe
    
    
    @classmethod
    def rolling_beta(cls,tickers="",window="",start_date="",end_date=""):
    
        """ Enter the Stock and Index in order"""
        rolling_beta_dict = {}
        
        if tickers and window is not None:
            
            #get prices and returns
            prices = GetPrices.yahoo(start_date,end_date,tickers)
            returns = Stats.get_one(prices,'daily returns')
                
                
            for i in window:
                
         
                rolling_variance = returns.iloc[0:,0].rolling(i).var()
                rolling_beta_dict[f"{tickers[0]}:{i}rolling variance"] = rolling_variance

                rolling_covariance = returns.iloc[0:,0].rolling(i).cov(returns.iloc[0:,1])
                rolling_beta_dict[f"{tickers[0]}:{i}rolling covariance"] = rolling_covariance


                rolling_beta = rolling_covariance / rolling_variance
                rolling_beta_dict[f"{tickers[0]}:{i}rolling beta"] = rolling_beta
#                 rolling_beta_dict["Index"] = tickers[1]
                    
        else:
            rolling_beta_dict['No rolling window params passed'] = 'No rolling window params passed'

        #dataframe = pd.DataFrame(rolling_beta_dict,index=[i for i in range(len(rolling_beta_dict.keys()))])
            
        return rolling_beta_dict
    

    
    @classmethod
    def get_all(cls,dataframe,tickers='',window=''):
        
        """Runs multiple calc types(see below) for each asset in dataframe. Returns a dictonary of dfs for each calc.
        Returns a dictonary containing all calc types as key and result as value. 
    
        *For beta, enter the two tickers to use. Comparison is left to right(AAPL,SPY).  
            
        Args:
        
        -dataframe ('df'): Dataframe of closing prices.
        -beta_tickers ('list'): 
        
        Returns:

        -dictonary of results for each calc type.  

        Calc Types:

        -daily returns,-daily returns avg,-cumulative,-std,-std annualized,-natural log,-natural log avg,-natural log std
        -correlation, -sharpe ratio -sharpe ratio crypto
        """
        
        calc_dict = {
                    'daily returns':dataframe.pct_change(),
                    'daily returns avg':dataframe.pct_change().mean(),
                    'cumulative': (1 + dataframe.pct_change()).cumprod().dropna(),
                    'std':dataframe.pct_change().std(),
                    'std annualized':(dataframe.pct_change()*np.sqrt(365)).sort_values(by="Date"),
                    'natural log':np.log(dataframe/dataframe.shift(1)),
                    'natural log avg':np.log(dataframe/dataframe.shift(1).mean()),
                    'natural log std':np.log(dataframe/dataframe.shift(1).std()),
                    'correlation':dataframe.pct_change().corr(),
                    'sharpe ratio':((dataframe.pct_change().mean() * 252)/(dataframe.std() * np.sqrt(252))),
                    'sharpe ratio crypto':((dataframe.pct_change().mean() * 365)/(dataframe.std() * np.sqrt(365))),
                    'beta':self.beta(tickers),
                    'rolling beta':self.rolling_beta(tickers,window)
                    }

        return calc_dict
    
    
    @classmethod
    def get_one(cls,dataframe,calc_type='',tickers='',window=''):
        
        """Calculates the given calc type for each value in df. Returns a with the results
        Returns a single dataframe. 
        
        Args:

        -dataframe ('df'): Dataframe of closing prices.
        -calc_type ('str'): Single calc type. 
        
        Returns:
    
        -dataframe: Dataframe of calc_type results. 

        Calc Types:

        -daily returns,-daily returns avg,-cumulative,-std,-natural log,-natural log avg,-natural log std
        -correlation, -sharpe ratios
        """
        
        calc_dict = {
                    'daily returns':dataframe.pct_change(),
                    'daily returns avg':dataframe.pct_change().mean(),
                    'cumulative': (1 + dataframe.pct_change()).cumprod().dropna(),
                    'std':dataframe.pct_change().std(),
                    'std annualized':(dataframe.pct_change()*np.sqrt(365)).sort_values(by="Date"),
                    'natural log':np.log(dataframe/dataframe.shift(1)),
                    'natural log avg':np.log(dataframe/dataframe.shift(1).mean()),
                    'natural log std':np.log(dataframe/dataframe.shift(1).std()),
                    'correlation':dataframe.pct_change().corr(),
                    'sharpe ratio':((dataframe.pct_change().mean() * 252)/(dataframe.std() * np.sqrt(252))),
                    'sharpe ratio crypto':((dataframe.pct_change().mean() * 365)/(dataframe.std() * np.sqrt(365))),
                    'beta':self.beta(tickers),
                    'rolling beta':self.rolling_beta(tickers,window)
                    }

        if calc_type in calc_dict:
            
            dataframe = pd.DataFrame(calc_dict[calc_type])
            
        else:
            print(f"These are the allowable types! : {list(calc_dict.keys())}")
                
        return dataframe


