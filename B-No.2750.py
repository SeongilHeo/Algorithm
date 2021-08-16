# src: https://www.acmicpc.net/problem/2750
n=int(input())
a=[int(input()) for _ in range(n)]
a.sort()
for x in a:
    print(x)