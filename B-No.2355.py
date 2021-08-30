# src: https://www.acmicpc.net/problem/2355
a,b=map(int,input().split())
if a>b:
    a,b=b,a
r=-1
if a*b<0:# - +
    t=b-abs(a)
    if t==0:
        r=0
    elif t<0:
        b=-b-1
    else:
        a=-a+1
if r==-1:
    if a<0:
        r=(a+b)/2*(-a+b+1)
    else:
        r=(a+b)/2*(b-a+1)
print(int(r))