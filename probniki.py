
def primes():
    import itertools
    a=2
    while True:
        n=0
        for i in range(1,a):
            if a%i ==0:
                n+=1
        if n==1:
            yield a
            a+=1
        a+=1
print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
