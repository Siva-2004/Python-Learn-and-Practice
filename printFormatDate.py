import datetime

date = datetime.datetime(2022,4,12)
result = datetime.datetime.strftime(date,'%A %d %m %y')
print(result)