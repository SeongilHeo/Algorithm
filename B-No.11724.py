# src: https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
 
N,M=map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited  = [False] * (1+N)
cnt=0       

for i in range(1,N+1):
    if not visited[i]:
        if not graph[i]:
            cnt+=1
            visited[i]=True
        else:
            dfs(i)
            cnt+=1
print(cnt)