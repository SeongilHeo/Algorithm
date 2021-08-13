# src: https://www.acmicpc.net/problem/1267
from math import ceil
c=int(input())
L=list(map(int,input().split()))
Y,M=0,0
for l in L:
    if l%30==0:
        l+=0.5
    Y+=ceil(l/30)*10
    M+=ceil(l/60)*15
if Y>M:
    print("M %d"%M)
elif M>Y:
    print("Y %d"%Y)
else:
    print("Y M %d"%Y)