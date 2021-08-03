# src: https://www.acmicpc.net/problem/2751
N=int(input())
L=[int(input()) for _ in range(N)]
L.sort()
for x in L:
    print(x)