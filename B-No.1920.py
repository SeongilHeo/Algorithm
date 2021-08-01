# src: https://www.acmicpc.net/problem/1920
N=int(input())
n=list(map(int,input().split()))
M=int(input())
m=list(map(int,input().split()))
n.sort()
for x in m:
    s,mid,e=-1,0,N
    while True:
        mid=(s+e)//2
        if n[mid]>x:
            e=mid
        elif n[mid]<x:
            s=mid
        else:
            print(1)
            break
        if e-s==1:
            print(0)
            break    