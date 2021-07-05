# src: https://www.acmicpc.net/problem/2775
A=[list(range(1,15))]+[[0]*14 for _ in range(14)]
for i in range(1,15):
    for j in range(14):
        A[i][j]=sum(A[i-1][:j+1])
        
n=int(input())

for _ in range(n):
    k=int(input()) # Ãþ
    n=int(input()) # È£
    print(A[k][n-1])