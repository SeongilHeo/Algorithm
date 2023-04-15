 src: https://www.acmicpc.net/problem/9461
n=int(input())
dp=[1,1,1,2,2,3,4,5,7,9,12]
for i in range(10,101):
    dp.append(dp[i-1]+dp[i-2])
for _ in range(n):
    print(dp[int(input())-1])