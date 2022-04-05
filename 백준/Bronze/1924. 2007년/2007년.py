import datetime
import time
month, dayy = map(int,input().split())
def d(a,b,c):
    daylist = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return daylist[datetime.date(a,b,c).weekday()]
dd = d(2007,month, dayy)
print(f"{dd}")
