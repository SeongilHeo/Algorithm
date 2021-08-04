# src: https://www.acmicpc.net/problem/1929
m,n=map(int,input().split())
L=list(range(m,n+1))

def func(x):
    if x<2:
        return False
    for i in range(2,int(x**(1/2))+1):
        if x%i==0:
            return False
    return True

for i in L:
    if func(i):
        print(i)