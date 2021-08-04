# src: https://www.acmicpc.net/problem/10814
n=int(input())
L=[input().split() for _ in range(n)]

L.sort(key=lambda x:int(x[0]))

for age,name in L:
    print(age,name)