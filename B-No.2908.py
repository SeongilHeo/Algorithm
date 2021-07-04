# src: https://www.acmicpc.net/problem/2908
a,b=input().split()
A,B=int(a[::-1]),int(b[::-1])
print(max(A,B))