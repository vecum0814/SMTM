import pandas as pd 
index = pd.date_range(start = '2019-01-01', end = '2019-10-01', freq = 'B')
series = pd.Series(range(len(index)), index = index)

print(series)