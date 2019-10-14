import os
import pandas as pd
import numpy as np

class bitcoinanalyzer:

    def create_portfolio(self,dataframes):
        self.portfolio=pd.concat(dataframes,axis='columns',join='inner').dropna()
    
    def concat_dataframes(self,dataframes,axisvalue):
        return pd.concat(dataframes,axis=axisvalue,join='inner').dropna()

    def drop_nulls(self,dataframe):
       dataframe.dropna(inplace=True)

    #Calculate daily returns
    def calculate_daily_returns(self,dataframe):
        return dataframe.pct_change().dropna()

    ## Removes currency symbol from the values
    def remove_currency_sign(self,dataframe,colname,currencysymbol):
        dataframe[colname]=dataframe[colname].str.replace(currencysymbol,'')

    #Calculates cumulative total based on daily returns
    def calculate_cumulative_returns(self,dailyreturns):
        return (1 + dailyreturns).cumprod().dropna()

    def change_column_datatype(self,dataframe,colname,newdatatype):
        dataframe[colname]=dataframe[colname].astype(newdatatype)

    def rename_columns(self,dataframe,columnmapper):
        dataframe.rename(columns=columnmapper,inplace=True)

    def calculate_standard_devation(self,dailyreturns,sortascending=True):
        return dailyreturns.std().sort_values(ascending=sortascending)

    def calculate_annulized_standard_devation(self,dailyreturns,workingdays=365,sortascending=True):
        return (dailyreturns * np.sqrt(workingdays)).sort_values(ascending=sortascending)
    
    def calculate_rolling_standard_deviation(self,dataframe,daywindow):
        return dataframe.rolling(window=daywindow).std()

    def calculate_correlation(self,dataframe):
        return dataframe.corr()
    
    def calculate_beta(self,dailyreturns,convarienceportfolio,varianceportfolio,workingdays=0):
        _covariance=0
        _variance=0
        _calculated_beta=0
        if (workingdays==0):
            _covariance=dailyreturns[convarienceportfolio].cov(dailyreturns[varianceportfolio])
            _variance=dailyreturns[varianceportfolio].var()
        else:
            _covariance=dailyreturns[convarienceportfolio].rolling(window=workingdays).cov(dailyreturns[varianceportfolio])
            _variance=dailyreturns[varianceportfolio].rolling(window=workingdays).var()
        _calculated_beta=_covariance/_variance
        return _calculated_beta
    
    def determine_risky_portfolio(self,stddata,baseportfolioname):
        return stddata.gt(stddata[baseportfolioname])
    
    def calculate_expotential_weighted_average(self,dataframe,halflifevalue):
        return dataframe.ewm(halflife=halflifevalue).std()
    
    def calculate_sharpie_ratio(self,dailyreturns):
        return (dailyreturns.mean() * 365) / (dailyreturns.std() * np.sqrt(365))

    def calculate_weighted_returns(self,dailyreturns,weights):
        return dailyreturns.dot(weights)
