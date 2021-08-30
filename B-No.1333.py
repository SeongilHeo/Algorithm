# src: https://www.acmicpc.net/problem/1333
n,l,d=map(int,input().split())
A=[0]*(n*(l+5)-5)
for i in range(n):
    s=(l+5)*i
    for j in range(s,s+l):
        A[j]=True
r=0
while r<len(A):
    if not A[r]:
        break
    r+=d
print(r)