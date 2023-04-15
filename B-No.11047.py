# src: https://www.acmicpc.net/problem/11047
N,K=map(int,input().split())
C=[]
for _ in range(N):
    C.append(int(input()))
C.sort(reverse=True)
idx=0
cnt=0
while K>=0 and idx<N:
    if K<C[idx]:
        idx+=1
        continue
    else:
        K-=C[idx]
        cnt+=1
print(cnt)