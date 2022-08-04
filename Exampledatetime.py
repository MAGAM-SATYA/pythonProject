import datetime
import time
print(time.time())
print(time.asctime(time.localtime(time.time())))
a=datetime.datetime.now()
print("year=",a.year)
print("month",a.month)
print("hour",a.hour)
print("minute",a.minute)
print("day",a.day)
import calendar
s=calendar.prcal(2022)
