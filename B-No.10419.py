# src: https://www.acmicpc.net/problem/10419
from math import ceil
n=int(input())
for _ in range(n):
    d=int(input())
    k=((1+4*d)**(1/2)-1)/2
    if k%1==0 :
        k+=1
    print(ceil(k)-1)