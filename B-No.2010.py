# src: https://www.acmicpc.net/problem/2010
import sys
input=sys.stdin.readline
n=int(input())
s=1
for _ in range(n):
    s+=int(input())-1
print(s)