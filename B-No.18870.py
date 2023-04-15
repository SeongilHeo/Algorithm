# src: https://www.acmicpc.net/problem/18870
n=int(input())
A=list(map(int,input().split()))
L=[[i,x,0] for i,x in enumerate(A)]
L.sort(key=lambda x:x[1])
cnt=0
for i in range(1,n):
    if L[i-1][1]==L[i][1]:
        L[i][2]=cnt
    else:
        cnt+=1
        L[i][2]=cnt
L.sort(key=lambda x:x[0])

for i in range(n):
    print(L[i][2],end=" ")