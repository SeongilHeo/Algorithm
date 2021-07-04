# src: https://www.acmicpc.net/problem/10952
a,b=map(int,input().split())
while a:
    print(a+b)
    try:
        a,b=map(int,input().split())
    except:
        break