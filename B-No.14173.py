# src: https://www.acmicpc.net/problem/14173
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=[min(a[0],b[0]),min(a[1],b[1]),max(a[2],b[2]),max(a[3],b[3])]
print(max(c[3]-c[1], c[2]-c[0])**2)