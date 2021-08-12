# src: https://www.acmicpc.net/problem/15128
a,b,c,d=map(int,input().split())
size=(a/b)*(c/d)*(1/2)
print(size)
if size%1:
    print(0)
else:
    print(1)