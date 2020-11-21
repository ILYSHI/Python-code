a=int(input())
print(a)
for i in range(1, 1001):
    if 5 <= i <= 20 or 11 <= i % 100 <= 14:
        print(i, 'программистов')
    elif 5 <= i % 10 <= 9 or i % 10 == 0:
        print(i, 'программистов')
    elif i % 10 == 1:
        print(i, 'программист')
    else:
        print(i, 'программиста')















