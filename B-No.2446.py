# src: https://www.acmicpc.net/problem/2446
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(2,n+1):
    print(" "*(n-i)+"*"*(2*i-1))