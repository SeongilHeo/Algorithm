# src: https://www.acmicpc.net/problem/3003
origin=[1,1,2,2,2,8]
L=list(map(int,input().split()))
print(*[origin[i]-L[i]for i in range(6)])