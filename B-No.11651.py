# src: https://www.acmicpc.net/problem/11651
import sys
input=sys.stdin.readline
n=int(input())
L=[list(map(int,input().split())) for _ in range(n)]
L.sort(key=lambda x:(x[1],x[0]))
for x,y in L:
    print(x,y)