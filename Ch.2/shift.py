import pandas as pd
import numpy as np
##aapl_df = pd.read_csv('/Users/raylee/SMTM/SMTM/Ch.2/us_data/AAPL.csv')
aapl_df = pd.read_csv('/Users/raylee/SMTM/SMTM/Ch.2/us_data/AAPL.csv', index_col='Date',parse_dates=['Date'])


aapl_df['Close_lag1'] = aapl_df['Adj Close'].shift()
print(aapl_df.head())