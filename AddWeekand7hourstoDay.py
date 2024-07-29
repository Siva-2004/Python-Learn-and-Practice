from datetime import datetime,timedelta

date = datetime(2021,3,14,7,0,0)

result = date + timedelta(days=7,hours=7)
print(result)