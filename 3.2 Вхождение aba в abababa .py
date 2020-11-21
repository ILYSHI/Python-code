s, t = (input() for _ in range(2))
i = 0
index = 0
while t in s[index:]:
    i+=1
    index+=s[index:].find(t)+1
print(i)


