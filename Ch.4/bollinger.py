import pandas as pd 
import matplotlib.pylab as plt

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

base_date = '2017-01-01'
sample = bollinger.loc[base_date:]
sample.head()

#sample = price_df.loc[base_date:]

book = sample[['Adj Close']].copy()
book['trade'] = '' #거래내역 칼럼
book.head()


def create_trade_book(sample):
    book = sample[['Adj Close']].copy()
    book['trade'] = ''
    return (book)


def tradings(sample, book):
    for i in sample.index:
        if sample.loc[i, 'Adj Close'] > sample.loc[i, 'ub']: # 상단밴드 이탈시 동작 안함
            book.loc[i, 'trade'] = ''
        elif sample.loc[i, 'lb'] > sample.loc[i, 'Adj Close']: # 하반밴드 이탈시 매수
            if book.shift(1).loc[i, 'trade'] == 'buy':    # 이미 매수상태라면
                book.loc[i, 'trade'] = 'buy'     # 매수상태 유지
            else:
                book.loc[i, 'trade'] = 'buy'    
        elif sample.loc[i, 'ub'] >= sample.loc[i, 'Adj Close'] and sample.loc[i, 'Adj Close'] >= sample.loc[i, 'lb']: # 볼린저 밴드 안에 있을 시
            if book.shift(1).loc[i, 'trade'] == 'buy':
                book.loc[i, 'trade'] = 'buy'  # 매수상태 유지
            else:
                book.loc[i, 'trade'] = '' # 동작 안함
    return (book)

book = tradings(sample, book)
book.tail(10)


#book.to_excel(excel_writer='./sample3.xlsx')

def returns(book):
    # 손익 계산
    rtn = 1.0
    book['return'] = 1
    buy = 0.0
    sell = 0.0
    for i in book.index:
        if book.loc[i, 'trade'] == 'buy' and book.shift(1).loc[i, 'trade'] == '':     # long 진입
            buy = book.loc[i, 'Adj Close']
            print('진입일 : ',i, 'long 진입가격 : ', buy)
        elif book.loc[i, 'trade'] == '' and book.shift(1).loc[i, 'trade'] == 'buy':     # long 청산
            sell = book.loc[i, 'Adj Close']
            rtn = (sell - buy) / buy + 1 # 손익 계산
            book.loc[i, 'return'] = rtn
            print('청산일 : ',i, 'long 진입가격 : ', buy, ' |  long 청산가격 : ', \
                  sell, ' | return:', round(rtn, 4))
    
        if book.loc[i, 'trade'] == '':     # zero position
            buy = 0.0
            sell = 0.0
    
    acc_rtn = 1.0
    for i in book.index:
        rtn = book.loc[i, 'return']
        acc_rtn = acc_rtn * rtn  # 누적 수익률 계산
        book.loc[i, 'acc return'] = acc_rtn

    print ('Accunulated return :', round(acc_rtn, 4))
    return (round(acc_rtn, 4))

print(returns(book))

book['acc return'].plot()
