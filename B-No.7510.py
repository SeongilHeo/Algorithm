# src: https://www.acmicpc.net/problem/7510
n=int(input())
for i in range(n):
    L=list(map(int,input().split()))
    L.sort()
    print("Scenario #%d:"%(i+1))
    if L[0]**2+L[1]**2==L[2]**2:
        print("yes")
    else:
        print("no")
    print()