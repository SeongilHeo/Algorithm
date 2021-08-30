# src: https://www.acmicpc.net/problem/2991
a,b,c,d=map(int,input().split())
p,m,n=map(int,input().split())

N=max(p,m,n)
A=[0]*N
for i in range(N):
    if i%(a+b)<a:
        A[i]+=1
    if i%(c+d)<c:
        A[i]+=1
print(A[p-1])
print(A[m-1])
print(A[n-1])