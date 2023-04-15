# src: https://www.acmicpc.net/problem/11727
dp=[0,1,3,5]
for i in range(4,1001):
    dp.append(dp[i-1]+dp[i-2]*2)
print(dp[int(input())]%10007)