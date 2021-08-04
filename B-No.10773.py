# src: https://www.acmicpc.net/problem/10773
import sys
input=sys.stdin.readline
n=int(input())
L=[int(input()) for _ in range(n)]
s=[]
for x in L:
    if s and x==0:
        s.pop()
    else:
        s.append(x)
print(sum(s))