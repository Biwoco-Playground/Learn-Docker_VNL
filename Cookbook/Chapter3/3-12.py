from datetime import timedelta
from datetime import datetime

a = timedelta(days=2,hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c)
print('day :',c.days,'hours :',c.seconds)
a = datetime(2000,3,30)
print(a)
print(a + timedelta(9))
print(datetime.today())
print(datetime.today()+timedelta(10))