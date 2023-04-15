# src: https://www.acmicpc.net/submit/1620/58941360
N,M = map(int, input().split())
D=dict()
L=list()
R=list()
for i in range(N):
    name=input()
    D[name]=i+1
    L.append(name)
for _ in range(M):
    q=input()    
    if D.get(q):
        r=D[q]
    else:
        r=L[int(q)-1]
    print(r)