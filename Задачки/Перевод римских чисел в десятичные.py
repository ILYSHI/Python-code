dict = {"I":1,
        'V':5,
        'X':10,
        "L":50,
        'C':100,
        'D':500,
        'M':1000
}

a = input()
sum = 0
i = 0
while i < len(a):
    if dict[a[i]]>dict[a[i-1]] and i>0:
        sum+=dict[a[i]]
        sum-=dict[a[i-1]]*2
        i+=1
    else:
        sum += dict[a[i]]
        i+=1
print(sum)




