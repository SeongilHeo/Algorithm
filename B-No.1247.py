# src: https://www.acmicpc.net/problem/1247
for _ in range(3):
    n=int(input())
    s=0
    for _ in range(n):
        s+=int(input())
    if s<0:
        print("-")
    elif s==0:
        print("0")
    else:
        print("+")