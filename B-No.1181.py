# src: https://www.acmicpc.net/problem/1181
N=int(input())
L=[input() for _ in range(N)]

L=list(set(L))
L.sort(key=lambda x:(len(x),x))

for x in L:
    print(x)