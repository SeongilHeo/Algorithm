# src: https://www.acmicpc.net/problem/1546
n=int(input())
L=list(map(int,input().split()))
M=max(L)
NL=list(map(lambda x:x/M*100,L))
print(round(sum(NL)/n,6))