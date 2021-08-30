# src: https://www.acmicpc.net/problem/2460
import sys
input=sys.stdin.readline
L=[]
while True:
    a=input()
    if not a:
        break
    L.append(list(map(int,a.split())))
P=[0]
for a,b in L:
    P.append(P[-1]-a+b)
print(max(P))