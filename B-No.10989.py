# src: https://www.acmicpc.net/problem/10989
import sys
input=sys.stdin.readline
n=int(input())
A=[0]*10001
for _ in range(n):
    x=int(input())
    A[x]+=1
for i,x in enumerate(A):
    if x!=0:
        for _ in range(x):
            print(i)