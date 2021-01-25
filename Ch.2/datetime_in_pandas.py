import pandas as pd 
print(pd.Timestamp(1239.1238934, unit = 'D'))
print(pd.Timestamp('2019-1-1'))
print(pd.to_datetime('2019-1-1 12'))
print(pd.to_datetime(['2018-1-1', '2019-1-2']))
print(pd.date_range('2019-01','2019-02'))

print(pd.Period('2019-01'))
print(pd.Period('2019-05', freq = 'D'))
print(pd.period_range('2019-01','2019-02',freq='D'))