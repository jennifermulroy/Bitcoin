# CryptoAnalyzer 
  ## Analysis on Bitcoin Trading History 

### Questions explored in this analysis: 
  1. Does Bitcoin's trading prices behavior more closely resemble that of a risky asset class or currency? 
  2. Is it possible to apply traditional statistical analysis used in financial data to Bitcoin's trading history?
  3. How does Bitoin’s return and risk profile compare to other risky assets?  
  4. Is Bitcoin correlated with other asset classes, or is it an idiosyncratic risk factor?
  5. Are there unique fundamental factors that drive Bitcoin's price, what are they? 
  6. Will Bitcoin continue to appreciate in value, and if so, does it add diversification to a portfolio? 

#### 1. Does Bitcoin's trading prices behavior more closely resemble that of a risky asset class or currency? 
 
 Bitcoin's price history has been extremely volatile; in fact, the most volatile of our selected asset classes. Bitcoin's daily price movements are so volatile they are six times more volatile than the equities which are considered at the higher end of the risk spectrum of risky assets. Conversely, currencies should not necessarily appreciate over time; but most importantly, should be stable over time. currency should be a store of value and a unit of transaction with its most prized attributed being price stable over time. 
 
 ![annualized returns and std](Images/annualized_returns_std.png)

  

![BTC_price_chart](Images/BTC_price_chart_inception.png)
![SPY_price_chart](Images/SPY_price_chart_inception.png)
![USD_price_chart](Images/USD_price_chart_inception.png)

 #### 2. Is it possible to apply traditional statistical analysis used in financial data to Bitcoin's trading history? 
 
Observations:
In securities analysis, a normal distribution of returns is assumed and sought in order to draw conclusions with a reasonable degree of confidence. We ran a visual plot of Bitcoin's daily returns since July 2010 and compared it against the S&P500, and a highly volatile semiconductor stock, AMD. 

Conclusion:
Based on the plot visuals, we can assume Bitcoin follows a normal distribution and therefore, can be analyzed with traditional statistical analysis.
 
 ![BTC_daily_returns](Images/Daily_returns_BTC_inception.png)
 
 ![BTC_histogram](Images/BTC_histogram_dailyreturns.png)
 
 ![ETH_daily_returns](Images/ETH_daily_returns_histogram.png)
 
 ![AMG_histogram](Images/AMD_daily_returns_histogram.png)
 
 #### 3. How does Bitoin’s return and risk profile compare to other risky assets?

We compared Bitcoin to the SPDR S&P 500 ETF (SPY), iShares Core U.S. Aggregate Bond ETF (AGG), US Dollar/USDX - Index, Bloomberg Commodity Index Total Return ETN (DJCI), and SPDR Gold Shares (GLD).
We looked at daily volatility, correlation, and the sharpe ratios on a five year, three year, and one year return basis from 10/1/2019. We also looked at the period from 10/1/2017-10/1/2018 when Bitcoin's price had its fastest rate of appreciation and pullback in price.  

Observations:
Bitcoin’s return profile has shown some superior absolute returns and risk-adjusted returns since inception and over some of our medium-term observation periods.  However – caveat emptor - as the data series had displayed a parabolic-like price appreciation in earlier years and appears to have been displaying a much different trend following its price peak. 

Conclusion:
Compared with our selected asset classes, Bitcoin has shown the best price appreciation and even risk-adjusted returns as measured by Sharpe ratio since inception and on a 3 and 5 year basis.  


Daily volatility and sharpe ratios over the last five years

 ![five_year_daily_vol](Images/daily_volatility_five.png)

![five_year_sharpe](Images/sharpe_five_plot.png)


Daily volatility and sharpe ratios over the last three years

 
 ![three_year_daily_vol](Images/daily_volatility_three.png)
 
 ![three_year_sharpe](Images/sharpe_three_plot.png)

 
Daily volatility and sharpe ratios over the last year

 
 ![One_year_daily_vol](Images/daily_volatility_one.png)
 
 
  
 ![One_year_sharpe](Images/sharpe_one_plot.png)

Daily volatility and sharpe ratios during Bitcoin's peak price period: 10/1/2017-10/1/2018

 
 ![Peak_year_daily_vol](Images/daily_volatility_peak.png)
  
 ![Peak_year_sharpe](Images/sharpe_peak_plot.png)
 

 #### 4. Is Bitcoin correlated with other asset classes, or is it an idiosyncratic risk factor? 
 
In terms of portfolio theory and portfolio construction, the addition of uncorrelated assets provides very valuable benefits of diversification and risk mitigation.  In fact, one of the most highly sought after and fleeting factors in alternative asset management is idiosyncratic risk.  Is bitcoin correlated with other risky assets and can it be a valuable component when included in a portfolio of risky assets?

Observations:
We ran cross asset correlations among our selected asset classes over 5, 3, and 1 year periods.  Bitcoin consistently shows very low correlations with all other asset classes.  Its correlations hover around zero with nearly all of our selected asset classes and over nearly all of our selected periods.  It certainly has the lowest correlations with all other asset classes vs. our selections.

Conclusion:
Bitcoin effectively has no discernible correlation with the range of risky assets we selected and over any of the periods we selected.  Bitcoin appears to be a unique idiosyncratic risk factor; and despite its volatility and uncertain trajectory, would likely provide diversification and hedging benefits if included in a portfolio of risky assets. 

Correlation over a 5 year period

![five_year_cor](Images/correlation_five_heatmap.png)

Correlation over a 3 year period

![three_year_cor](Images/correlation_three_heatmap.png)

Correlation over a 1 year period

![one_year_cor](Images/correlation_one_heatmap.png)

Correlation during Bitcoin's peak price period: 10/1/2017-10/1/2018 

![Peak_year_cor](Images/correlation_peak_heatmap.png)

 
 #### 5. Will Bitcoin continue to appreciate in value, and if so, does it add diversification to a portfolio? 
 
We ran a Monte Carlo simulation to forecast Bitcoin's price trajectory over the next 365 trading days, using Bitcoin's five year average daily returns and five year standard deviation of returns. There is a 95% chance that an initial investment of $10,000 in Bitcoin over the next 365 trading days will end within the range of $4,330.64 and $78,209.97 

![Monte_price](Images/Monte_BTC_price.png)

![Monte_price](Images/Monte_BTC_confidence_interval_plot.png)

We ran a Monte Carlo simulation for a diversified portfolio with Bitcoin and without to compare a five year return trajectory. 

Given an initial investment of $20,000, in an equally weighted portfolio of Bitcoin, SPDR S&P 500 ETF (SPY), iShares Core U.S. Aggregate Bond ETF (AGG), Bloomberg Commodity Index Total Return ETN (DJCI), and SPDR Gold Shares (GLD), the expected portfolio return in dollars at the 10th percentile: $45,950.42, at the 50th percentile $58,741.36, and at the 90th percentile: $76,136.19

Given the same initial investment of $20,000, in an equally weighted portfolio of the same assets without Bitcoin, the expected portfolio return in dollars at the 10th percentile: $38,122.49, at the 50th percentile $41,640.88, and at the 90th percentile: $45,503.43

In conclusion, Bitcoin has the potential to significantly increase in value over time. It is uncorrelated with other risky assets and provides diversification to a portfolio. And based on Monte Carlo simulations, if added to a diversfied portfolio can potentially provide additional returns. 
 

