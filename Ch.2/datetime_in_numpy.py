# str 타입은 ISO 8601 형식에 맞춰서 사용해야 한다.
import numpy as np
day = np.datetime64('2019-01-01')
print(day)
print(np.datetime64(1000,'ns'))
print(np.datetime64(10000,'D'))
print(np.datetime64(1000000000,'s'))

print(np.array(['2007-07-13', '2006-01-13', '2010-08-13'], dtype = 'datetime64'))

print(np.arange('2005-02', '2005-03', dtype = 'datetime64[D]'))

print(np.arange('2005-02', '2006-03', dtype = 'datetime64[M]'))

print(np.datetime64('2009-01-01') - np.datetime64('2008-01-01'))
print(np.datetime64('2009') - np.datetime64('2008-01'))
print(np.datetime64('2009-01-01') - np.datetime64('2008-01'))