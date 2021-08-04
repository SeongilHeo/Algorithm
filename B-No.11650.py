# src: https://www.acmicpc.net/problem/11650
n=int(input())
L=[list(map(int,input().split())) for _ in range(n)]

L.sort(key=lambda x: (x[0],x[1]))

for x,y in L:
    print(x,y)