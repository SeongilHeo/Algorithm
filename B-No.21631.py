# src: https://www.acmicpc.net/problem/21631
a,b=map(int,input().split())
if a>=b:
    print(b)
else:
    print(a+1)