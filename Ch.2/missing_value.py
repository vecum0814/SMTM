import pandas as pd
import numpy as np

s1 = pd.Series([1,np.nan,3,4,5])
s2 = pd.Series([1,2,np.nan,4,5])
s3 = pd.Series([1,2,3,np.nan,5])
df = pd.DataFrame({'S1':s1, 
                   'S2':s2,
                   'S3':s3
                  })

print(df.head())
##print(df['S1'].isna())
##print(df.isna())
##print(df.isna().sum())

##print(df.fillna(0))
print(df.fillna(method='pad'))