def hanoi(q,fromm,to,buf):
    if q == 1:
        print(fromm,'-',to)
    else:
        hanoi(q-1,fromm,buf,to)
        print(fromm, '-', to)
        hanoi(q - 1, buf, to, fromm)
n = int(input())
hanoi(n,1,3,2)
