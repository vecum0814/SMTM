import pandas as pd
import numpy as np
df = pd.read_csv('/Users/raylee/SMTM/SMTM/us_data/AMZN.csv', index_col='Date', parse_dates=['Date'])
#df.head()
#df[df.isin([np.nan, np.inf, -np.inf]).any(1)]

price_df = df.loc[:,['Adj Close']].copy()
#price_df.plot(figsize=(16,9))

price_df['daily_rtn'] = price_df['Adj Close'].pct_change()
#price_df.head(10)

price_df['st_rtn'] = (1 + price_df['daily_rtn']).cumprod()
#price_df.head(10)

#CAGR = price_df.loc['2020-10-24', 'st_rtn']**(252./len(price_df.index))-1

historical_max = price_df['Adj Close'].cummax()
daily_drawdown = price_df['Adj Close'] / historical_max - 1.0
historical_dd = daily_drawdown.cummin()
#historical_dd.plot()

CAGR = price_df.loc['2021-01-22', 'st_rtn'] ** (252./len(price_df.index)) -1
Sharpe = np.mean(price_df['daily_rtn']) / np.std(price_df['daily_rtn']) * np.sqrt(252.)
VOL = np.std(price_df['daily_rtn']) * np.sqrt(252.)
MDD = historical_dd.min()
print('CAGR : ',round(CAGR*100,2),'%')
print('Sharpe : ',round(Sharpe,2))
print('VOL : ',round(VOL*100,2),'%')
print('MDD : ',round(-1*MDD*100,2),'%')