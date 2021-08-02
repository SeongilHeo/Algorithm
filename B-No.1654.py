# src: https://www.acmicpc.net/problem/1654
K,N=map(int,input().split())
L=[int(input()) for _ in range(K)]

a,c=1,max(L)
r=0
while a<=c:
    b=(a+c)//2
    if sum([x//b for x in L])>=N:
        if r<b:
            r=b
        a=b+1
    else:
        c=b-1
print(r)