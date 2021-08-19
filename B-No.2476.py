# src: https://www.acmicpc.net/problem/2476
n=int(input())
M=0
for _ in range(n):
    a,b,c=map(int,input().split())
    r=0
    if a==b==c:
        r=10000+a*1000
    elif a==b:
        r=1000+a*100
    elif a==c:
        r=1000+a*100
    elif b==c:
        r=1000+b*100
    else:
        r=max(a,b,c)*100
    M=max(M,r)
print(M)