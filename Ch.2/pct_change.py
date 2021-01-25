import pandas as pd
import numpy as np
aapl_df = pd.read_csv('/Users/raylee/SMTM/SMTM/Ch.2/us_data/AAPL.csv', index_col='Date',parse_dates=['Date'])

aapl_df['Close_lag1'] = aapl_df['Close'].shift()
aapl_df['pct_change'] = aapl_df['Close'].pct_change()
aapl_df['Close_diff'] = aapl_df['Close'].diff()
aapl_df['MA'] = aapl_df['Close'].rolling(window = 5).mean()
aapl_df.to_excel(excel_writer='./sample.xlsx')

print(aapl_df.head(10))