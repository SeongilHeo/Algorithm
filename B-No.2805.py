# src: https://www.acmicpc.net/problem/2805
N,M=map(int,input().split())
L=list(map(int,input().split()))

a,c=0,max(L)
R=0
while a<=c:
    b=(a+c)//2
    t=sum(map(lambda x:x-b if x-b>=0 else 0,L))
    if M<=t:
        R=max(b,R)
        a=b+1
    else:
        c=b-1
print(R)