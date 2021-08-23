# src: https://www.acmicpc.net/problem/2606
import sys
input=sys.stdin.readline
c=int(input())
n=int(input())
L=[0]*c
t=1
for k in range(n):
    a,b=map(int,input().split())
    if L[a-1]==0 and L[b-1]==0:
        L[a-1]=L[b-1]=t
        t+=1
    elif L[a-1]==L[b-1]:
        pass
    elif L[a-1]!=0 and L[b-1]!=0:
        for i in range(c):
            if i!=b-1 and L[i]==L[b-1]:
                L[i]=L[a-1]
        L[b-1]=L[a-1]
    else:
        L[a-1]=L[b-1]=L[a-1]+L[b-1]
c=0
for i in L[1:]:
    if i==L[0]:
        c+=1
print(c)