# src: https://www.acmicpc.net/problem/2501
n,k=map(int,input().split())

c=0
r=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        if c==k:
            r=i
            break
print(r)