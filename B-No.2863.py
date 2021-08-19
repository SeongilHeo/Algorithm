# src: https://www.acmicpc.net/problem/2863
a,b=map(int,input().split())
c,d=map(int,input().split())
A=[a/c+b/d,c/d+a/b,d/b+c/a,b/a+d/c]
m=[0,-1]
for i,x in enumerate(A):
    if m[1]<x:
        m=i,x
print(m[0])
