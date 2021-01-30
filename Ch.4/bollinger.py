import pandas as pd 
df = pd.read_csv('/Users/raylee/SMTM/SMTM/us_data/SPY (1).csv')
df.head()
df.describe()

##데이터 가공 -> 날짜, 수정 종가를 선택 및 추출하고 copy() 함수를 사용해 복사한다.
price_df = df.loc[:,['Date','Adj Close']].copy()
#price_df.head() 

price_df.set_index(['Date'],inplace=True)
#price_df.head()

#price_df['center'] = price_df['Adj Close'].rolling(window = 20).mean()
#price_df.iloc[18:25]

#price_df['ub'] = price_df['center'] + 2 * price_df['Adj Close'].rolling(window = 20).std()
#price_df['lb'] = price_df['center'] - 2 * price_df['Adj Close'].rolling(window = 20).std()
#price_df.iloc[18:25]

n = 20
sigma = 2
def bollinger_band(price_df, n, sigma):
    bb = price_df.copy()
    bb['center'] = price_df['Adj Close'].rolling(n).mean() #중앙 이동평균선
    bb['ub'] = bb['center'] + sigma * price_df['Adj Close'].rolling(n).std() # 상단 밴드
    bb['lb'] = bb['center'] - sigma * price_df['Adj Close'].rolling(n).std() # 하단 밴드
    return bb

bollinger = bollinger_band(price_df, n, sigma)
bollinger.head(51)

base_date = '2021-01-01'
sample = bollinger.loc[base_date:]
sample.head()