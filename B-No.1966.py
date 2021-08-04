# src: https://www.acmicpc.net/problem/1966
N=int(input())
for _ in range(N):
    n,th=map(int,input().split())
    L=[(i,int(x)) for i, x in enumerate(input().split())]
    R=[]
    while L:
        t=L.index(max(L,key=lambda x:x[1]))
        R.append(L[t])
        L=L[t+1:]+L[:t]
        
    for i in range(n):
        if R[i][0]==th:
            print(i+1)
            