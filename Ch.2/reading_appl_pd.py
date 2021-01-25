import pandas as pd
df = pd.read_csv('/Users/raylee/SMTM/SMTM/Ch.2/us_data/AAPL.csv')
print(df.head()) 

aapl_df = pd.read_csv('/Users/raylee/SMTM/SMTM/Ch.2/us_data/AAPL.csv', index_col='Date',parse_dates=['Date'])

print(aapl_df.head())
print(type(aapl_df.index))
print(type(aapl_df.index[0]))
