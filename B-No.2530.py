# src: https://www.acmicpc.net/problem/2530
a,b,c=map(int,input().split())
t=int(input())
c=c+t
b+=c//60
c=c%60

a+=b//60
b=b%60
if a>23:
    a%=24
print(a,b,c)