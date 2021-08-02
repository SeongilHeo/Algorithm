# src: https://www.acmicpc.net/problem/2535
N=int(input())
L=[list(map(int,input().split())) for _ in range(N)]

L.sort(key=lambda x:-x[2])

D={x:0 for x in list(zip(*L))[0]}

i=0
for a,b,c in L:
    if i==3:
        break
    if D[a]<2:
        D[a]+=1
        print(a,b)
        i+=1 