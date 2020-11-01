import datetime

#timedelta
print(datetime.date(9999,12,31))
print(datetime.date.today())
print(datetime.datetime.today())
print(datetime.datetime.now())
todayDate =datetime.datetime.today()
print(datetime.timedelta(todayDate,days=3))