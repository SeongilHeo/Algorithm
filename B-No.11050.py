# src: https://www.acmicpc.net/problem/11050
N,K=map(int,input().split())
R=1
for i in range(K):
    R*=(N-i)
for i in range(1,K+1):
    R//=i
print(R)