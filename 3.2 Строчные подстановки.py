s, a, b = (input() for _ in range(3))
i = 0
while a in s and i<1000:
    i += 1
    s = s.replace(a,b)
    if i == 1000:
        print('Impossible')
if i<1000:
    print(i)