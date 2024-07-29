import datetime

Date = "Feb 23 1921 10:20AM"
print(datetime.datetime.strptime(Date,'%b %d %Y %I:%M%p'))