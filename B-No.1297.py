# src: https://www.acmicpc.net/problem/1297
a,b,c=map(int,input().split())
r=(a**2/(b**2+c**2))**(1/2)
print(int(b*r),int(c*r))