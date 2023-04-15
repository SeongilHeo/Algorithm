 src: https://www.acmicpc.net/problem/9095
dp=[0,1,2,4]
for i in range(4,12):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])
n=int(input())
for _ in range(n):
    x=int(input())
    print(dp[x])