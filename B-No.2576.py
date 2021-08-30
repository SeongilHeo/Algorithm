# src: https://www.acmicpc.net/problem/2576
import sys
input=sys.stdin.readline
s=0
m=101
for _ in range(7):
    a=int(input())
    if a%2:
        s+=a
        m=min(m,a)
if m==101:
    print(-1)
else:
    print(s)
    print(m)