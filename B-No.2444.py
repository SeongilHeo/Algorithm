# src: https://www.acmicpc.net/problem/2444
n=int(input())
for i in range(n-1):
    print(" "*(n-i-1)+"*"*(2*i+1))
for i in range(n-1,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))