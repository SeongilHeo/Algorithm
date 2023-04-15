# src: https://www.acmicpc.net/problem/1927
import heapq
import sys
input=sys.stdin.readline

H=[]
n=int(input())
R=0
for _ in range(n):
    x =int(input())
    if x ==0:
        if len(H):
            R=heapq.heappop(H)
        else:
            R=0
        print(R)
    else:
        heapq.heappush(H,x)
