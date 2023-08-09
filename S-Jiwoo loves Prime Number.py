import sys
import math
import heapq

input=sys.stdin.readline

N,M=map(int,(input().split()))
G=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int, input().split())
    G[a].append([b,c])
    G[b].append([a,c])

def dijkstra(start):
    d = [math.inf]*(N+1)
    d[start]=0
    H=[[0,start]] # make_heap(nodes v of G with key d[v])
    while H: # n iterations
        prev_dist,u = heapq.heappop(H)
        if d[u] < prev_dist:
            continue
        for v,dist in G[u]: # m edges are scanned in total
            next_dist=max(dist,prev_dist)
            if next_dist < d[v]:
                d[v] = next_dist
                heapq.heappush(H,[d[v],v])
    return d[-1]+1

def isPrime(num):
    for i in range(2, num//2+1):
        if num%i==0:
            return False
    return True

level=dijkstra(1)

while not isPrime(level):
    level+=1
print(level)