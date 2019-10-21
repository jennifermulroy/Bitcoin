# CryptoAnalyzer 
  ## Data Analysis on Bitcoin 

### In this analysis, we sought to answer these questions: 
  1. What is Bitcoin? Is it an asset or currency? 
  2. Can we apply traditional statistical analysis used in financial data to Bitcoin's trading history?
  3. How does Bitcoin compare against other risky asset classes? 
  4. Are there unique fundamental factors that drive Bitcoin's price, what are they? 
  5. Will Bitcoin continue to appreciate in value, and if so, does it add diversification to a portfolio? 

#### 1. What is Bitcoin, is it an asset or currency?

Currency is a store of value and shouldn't appreicate over time. Comparing the price chart of Bitcoin to the S&P500, Bitcoin has signficiantly appreciated in value similar to the equity market.  

![BTC_price_chart](Images/BTC_price_chart_inception.png)
![SPY_price_chart](Images/SPY_price_chart_inception.png)

 #### 2. Can we apply traditional statistical analysis used in financial data to Bitcoin's trading history? 
 
 In stock market analysis, a normal distribution of returns is assumed. We ran a visual plot of Bitcoin's daily returns since July 2010 and compared it against the S&P500, and a highly volatile semiconductor stock, AMD. 
 Based on the plot visuals, we can assume Bitcoin follows a normal distribution and therefore, can apply traditional statistical analysis.
 
 ![BTC_daily_returns](Images/Daily_returns_BTC_inception.png)
 
 ![BTC_histogram](BTC_histogram_dailyreturns.png)
 
 ![ETH_daily_returns](Images/ETH_daily_returns_histogram.png)
 
 ![AMG_histogram](AMD_daily_returns_histogram.png)
 
 #### How does Bitcoin compare against other risky asset classes? 

We compared Bitcoin to the S&P500 ETF, SPY
We looked at daily volatility, correlation, and the sharpe ratios on a five year, three year, and one year return basis from 10/1/2019.
We also carved out the period Bitcoin reached its all-time high in Dec 2017

Bitcoin's Sortino Ratio: 0.0879 from inception 

Daily Volatility over the last five years

