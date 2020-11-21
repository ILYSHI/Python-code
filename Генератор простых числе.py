import itertools
def kol_del(a):
    n=0
    for i in range(1,a):
        if a%i ==0:
            n+=1
    return n

def primes():
    a=2
    while True:
        if kol_del(a)==1:
            yield a
        a+=1
yo = primes()
for i in range(1000):
    print (next(yo))
print(list(itertools.takewhile(lambda x : x <= 1000, primes())))