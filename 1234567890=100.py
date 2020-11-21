a=[1,'',2,'',3,'',4,'',5,'',6,'',7,'',8,'',9,'',0]
b=['+','-','/','*',' ']
c=[1,'',2,'',3,'',4,'',5,'',6,'',7,'',8,'',9,'',0]
skolko=int(input())


#ищет в массиве деление
def dele(a):
    for i in range(len(a)):
        if a[i] == '/':
            if a[i + 1] == 0:
                a=[0]
                return(a)
            else:
                a[i - 1] = a[i - 1] / a[i + 1]
                for t in range(i, len(a)):
                    a[t] = a[t + 2 - len(a)]
                del a[-1]
                del a[-1]
                return dele(a)
    return a



def prob(a):
    for i in range(len(a)):
            if a[i]==' ':
                a[i-1]=a[i-1]*10+a[i+1]
                for t in range(i,len(a)):
                    a[t]=a[t+2-len(a)]
                del a[-1]
                del a[-1]
                return prob(a)
    return(a)
def mnozh(a):
    for i in range(len(a)):
            if a[i]=='*':
                a[i-1]=a[i-1]*a[i+1]
                for t in range(i,len(a)):
                    a[t]=a[t+2-len(a)]
                del a[-1]
                del a[-1]
                return mnozh(a)
    return(a)
def plus(a):
    for i in range(len(a)):
            if a[i]=='+':
                a[i-1]=a[i-1]+a[i+1]
                for t in range(i,len(a)):
                    a[t]=a[t+2-len(a)]
                del a[-1]
                del a[-1]
                return plus(a)
    return(a)
def minus(a):
    for i in range(len(a)):
            if a[i]=='-':
                a[i-1]=a[i-1]-a[i+1]
                for t in range(i,len(a)):
                    a[t]=a[t+2-len(a)]
                del a[-1]
                del a[-1]
                return minus(a)
    return(a)
n=0
for i in b:
    a[1]=i
    for i in b:
        a[3]=i
        for i in b:
            a[5]=i
            for i in b:
                a[7]=i
                for i in b:
                    a[9]=i
                    for i in b:
                        a[11]=i
                        for i in b:
                            a[13]=i
                            for i in b:
                                a[15]=i
                                for i in b:
                                    a[17]=i
                                    for i in range(len(a)):
                                        c[i] = a[i]
                                    prob(c)
                                    dele(c)
                                    mnozh(c)
                                    minus(c)
                                    plus(c)
                                    if c[0] == skolko and len(c)==1:
                                        for i in a:
                                            if i!=" ":
                                                print(i,end="")
                                        print("="+str(skolko))
                                        n += 1
                                    c = [1, '', 2, '', 3, '', 4, '', 5, '', 6, '', 7, '', 8, '', 9, '', 0]
print(n)
