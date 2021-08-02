# src: https://www.acmicpc.net/problem/1263
N=int(input())
L=[]
for _ in range(N):
    a,b=map(int,input().split())
    L.append((b-a,a,b))

L.sort(key=lambda x:-x[2])

start=L[0][0]
for a,b,c in L[1:]:
    if start < c:
        start=a-(c-start)
    else:
        start=a
print(start if start>=0 else -1)