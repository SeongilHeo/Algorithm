# src: https://www.acmicpc.net/problem/11726
dp=[0,1,2]
for i in range(3,1000):
    dp.append(dp[i-1]+dp[i-2])
print(dp[int(input())]%10007)