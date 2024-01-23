import time

print(time.time())
print(time.ctime(1704531563.172574))
a = time.localtime()
b = time.mktime(a)
print(b)
c = time.asctime(a)
print(c)
print(a)


x = time.strftime("%m/%d/%Y")
print(x)

y = "06 January 2024"
s = time.strptime(y, "%d %B %Y")
print(s)

# DateTime
import datetime

print(datetime.datetime(2019, 6, 7, 4, 30, 54, 678))

print(datetime.datetime.today())

v = datetime.datetime.now()
print(v.year)
print(v.month)
print(v.hour)

print(datetime.date(2024, 1, 6))
print(datetime.time(11, 36, 54))

b1 = datetime.timedelta(days=20)
b2 = datetime.timedelta(days=30)
b3 = b1 - b2
print(b3)
print(type(b3))
