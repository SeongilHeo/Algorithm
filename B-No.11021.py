# src: https://www.acmicpc.net/problem/11021
import sys

n=int(sys.stdin.readline().rstrip())
for i in range(n):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    print("Case #%d: %d"%(i+1,a+b))