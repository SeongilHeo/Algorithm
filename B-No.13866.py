# src: https://www.acmicpc.net/problem/13866
L=list(map(int,input().split()))
T=max(L)+min(L)
L=sum(L)
print(abs((L-T)-T))
