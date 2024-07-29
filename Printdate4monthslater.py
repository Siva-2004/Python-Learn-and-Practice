from datetime import datetime
from dateutil.relativedelta import relativedelta

date = datetime(2020,2,25).date()

result = date + relativedelta(months=4)
print(result)