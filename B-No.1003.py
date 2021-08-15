# src: https://www.acmicpc.net/problem/1003
import sys
input=sys.stdin.readline
n=int(input())
l=[int(input()) for _ in range(n)]
dp=[[0,0] for _ in range(max(l)+1)]
dp[0]=[1,0]
dp[1]=[0,1]
for i in range(2,len(dp)):
    dp[i][0]=dp[i-1][0]+dp[i-2][0]
    dp[i][1]=dp[i-1][1]+dp[i-2][1]
for i in l:
    print(dp[i][0],dp[i][1])