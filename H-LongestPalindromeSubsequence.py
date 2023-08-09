# 2023-05-23
# src: 2023-1 Algorithm TA
L=list(input())
n=len(L)
dp=[[0]*n for _ in range(n)]

for j in range(n):
    for i in range(j,-1,-1):
        if j==i:
            dp[i][j]=1
        else:
            if L[i]==L[j]:
                dp[i][j]=dp[i+1][j-1]+2
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j-1])

print(dp[0][-1])