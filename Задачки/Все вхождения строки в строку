import re

a = input()
b = input()
lst=[]
for i in range(len(a)):
    start = re.search(b,a[i:])
    if start != None:
        lst.append(start.start()+i)
if len(lst)>0:
    print(*sorted(set(lst)))
else:
    print(-1)