# src: https://www.acmicpc.net/problem/2525
a,b=map(int,input().split())
c=int(input())
b=b+c
a+=b//60
b=b%60
if a>23:
    a%=24
print(a,b)