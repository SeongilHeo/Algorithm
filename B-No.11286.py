# src: https://www.acmicpc.net/problem/11286
import sys
from heapq import heappop,heappush
input=sys.stdin.readline
n=int(input())
H=[]
for i in range(n):
    x=int(input())
    if x==0:
        if len(H)==0:
            r=0
        else:
            ar,r=heappop(H)
        print(r)    
    else:
        heappush(H,(abs(x),x))
