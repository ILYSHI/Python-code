a = [i for i in input().lower()]
b = [i for i in input().lower()]
a.sort()
b.sort()
flag = True
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            flag = False
else:
    flag = False
print(flag)