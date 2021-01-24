import datetime
format = '%Y-%m-%d %H:%M:%S'
datetime_str = '2018-05-13 12:34:56'
datetime_dt = datetime.datetime.strptime(datetime_str, format)


datetime_str = datetime_dt.strftime('%Y-%m-%d %H:%M:%S')
print(type(datetime_str))
print(datetime_str)