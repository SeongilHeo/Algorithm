# src: https://www.acmicpc.net/problem/2783
import sys
input =sys.stdin.readline
L=[]
L.append(list(map(int, input().split())))
n=int(input())
for _ in range(n):
    L.append(list(map(int, input().split())))
L.sort(key=lambda x:x[0]/x[1])
w,g=L[0]

print(round(w/g*1000,2))