# src: https://www.acmicpc.net/problem/21645
n,m,k=map(int,input().split())
if m < k:
    r=n*m
else:
    r=n*((k-1)+m//k)
print(r)