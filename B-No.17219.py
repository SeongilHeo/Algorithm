# src: https://www.acmicpc.net/problem/17219
N,M=map(int,input().split())
A=dict(input().split() for _ in range(N))
for _ in range(M):
    print(A[input()])
