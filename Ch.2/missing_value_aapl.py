import pandas as pd
import numpy as np
df = pd.read_csv('/Users/raylee/SMTM/SMTM/Ch.2/us_data/AAPL.csv',parse_dates=['Date'])
aapl_df = pd.read_csv('/Users/raylee/SMTM/SMTM/Ch.2/us_data/AAPL.csv', index_col='Date',parse_dates=['Date'])

##print(aapl_df[aapl_df.isin([np.nan, np.inf, -np.inf]).any(1)])

##print(df['Open'].head())

##print(df[['Open','High','Close']].head())

print(df['2020-10-10':'2020-10-20'])