# src: https://www.acmicpc.net/problem/16648
a,b=map(int,input().split())

if b<20:
    r=(120-2*b)/a
    print(b*2/r)
else:
    r=(100-b)/a
    print((b-20)/r+40/r)