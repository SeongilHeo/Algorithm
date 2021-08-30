# src: https://www.acmicpc.net/problem/1260
import sys
input=sys.stdin.readline

def dfs(l):
    for x in l:
        if x not in que:
            que.append(x)
            dfs(L[x])
            
n,m,v=map(int,input().split())
L=[list() for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    L[a].append(b)
    L[b].append(a)
for i in range(len(L)):
    L[i].sort()
que=[]
dfs([v])
for x in que:
    print(x,end=' ')
print()

que=[v]
t=0
while t<len(que):
    for x in L[que[t]]:
        if x not in que:
            que.append(x)
    t+=1
for x in que:
    print(x,end=' ')