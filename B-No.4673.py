# src: https://www.acmicpc.net/problem/4673
def d(x):
    return x+sum(list(map(int,str(x))))

A=dict(zip(range(1,10001),[True]*10000))

for i in range(10000):
    A[d(i)]=False

for i,x in A.items():
    if x==True:
        print(i)