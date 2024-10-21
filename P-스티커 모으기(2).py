# src: https://school.programmers.co.kr/learn/courses/30/lessons/12971
def solution(sticker):
    n=len(sticker)
    if n<4:
        return max(sticker)
    answer = 0

    dp=[0]*n
    dp[0]=sticker[0]
    dp[1]=sticker[0]
    for i in range(2,n-1):
        dp[i]=max(dp[i-1],dp[i-2]+sticker[i])
    answer=max(dp[-1],dp[-2])

    dp = [0] * n
    dp[0] = 0
    dp[1] = sticker[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    answer=max(answer,dp[-1],dp[-2])

    return answer