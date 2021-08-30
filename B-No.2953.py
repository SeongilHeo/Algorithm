# src: https://www.acmicpc.net/problem/2953
import sys
input=sys.stdin.readline
L=[]
i=0
while True:
    i+=1
    a=input()
    if not a:
        break
    L.append([i,sum(map(int,a.split()))])
print(*max(L,key=lambda x:x[1]))