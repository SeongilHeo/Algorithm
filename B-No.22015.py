# src: https://www.acmicpc.net/problem/22015
a,b,c=map(int,input().split())
m=max(a,b,c)
print(3*m-(a+b+c))