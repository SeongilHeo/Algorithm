# src: https://www.acmicpc.net/problem/2845
a,b=map(int,input().split())
L=list(map(int,input().split()))
p=a*b
print(*[x-p for x in L])