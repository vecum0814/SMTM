import datetime
format = '%Y-%m-%d %H:%M:%S'
datetime_str = '2018-05-13 12:34:56'
datetime_dt = datetime.datetime.strptime(datetime_str, format)
print(type(datetime_dt))
print(datetime_dt)


datetime_str = datetime_dt.strftime('%Y-%m-%d %H:%M')
print(type(datetime_str))
print(datetime_str)

datetime_str = datetime_dt.strftime('%Y-%m')
print(type(datetime_str))
print(datetime_str)