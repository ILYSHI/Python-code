import datetime
y, m , d = [int(i) for i in input().split(" ")]
a=datetime.date(y,m,d)
a+=datetime.timedelta(int(input()))
print(a.year,a.month,a.day)