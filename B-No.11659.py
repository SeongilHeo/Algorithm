# src: https://www.acmicpc.net/problem/11659
import sys
from math import log2,ceil
input=sys.stdin.readline
def node_init(A,size):
    for i in range(N):
        tree[size+i]=A[i]

    for i in range(size-1,0,-1):
        tree[i]=tree[i*2]+tree[i*2+1]
        
def sum(start,end,left,right,node):
    if right<start or end<left:
        return 0
    if left<=start and end<=right:
        return tree[node]
    mid=(start+end)//2
    return sum(start,mid,left,right,node*2)+sum(mid+1,end,left,right,node*2+1)

N,M=map(int, input().split())
A=list(map(int,input().split()))
size=2**ceil(log2(N))
tree=[0]*(size*2)

node_init(A,size)
for _ in range(M):
    start,end=map(int,input().split())
    print(sum(1,size,start,end,1))
