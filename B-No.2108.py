# src: https://www.acmicpc.net/problem/2108
import sys
input=sys.stdin.readline

n=int(input())

L=[]
D={}

for _ in range(n):
    x=int(input())
    L.append(x)
    if D.get(x):
        D[x]+=1
    else:
        D[x]=1

L.sort()

a=round(sum(L)/n)
b=L[n//2]
M=max(D.values())
t=sorted([x[0] for x in D.items() if x[1]==M])
c=t[1 if len(t)>1 else 0]
d=L[-1]-L[0]
print(a)
print(b)
print(c)
print(d)