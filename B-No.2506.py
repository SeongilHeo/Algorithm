# src: https://www.acmicpc.net/problem/2506
n=int(input())
L=list(map(int,input().split()))
r,t=0,0

for x in L:
    t+=1
    if x==0:
        t=0
    r+=t
print(r)