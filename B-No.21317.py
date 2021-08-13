# src: https://www.acmicpc.net/problem/21317
# ref: https://blog.naver.com/PostView.nhn?blogId=gustn3964&logNo=222303877311
N=int(input())
dp=[[9999999,9999999] for _ in range(N+4)]
jump=[tuple(map(int,input().split())) for _ in range(N-1)]
k=int(input())

dp[1]=[0,0]

for i in range(1,N):
    a,b=jump[i-1]
    for j in range(2):
        dp[i+1][j]=min(dp[i+1][j],dp[i][j]+a)
        dp[i+2][j]=min(dp[i+2][j],dp[i][j]+b)
    dp[i+3][1]=min(dp[i+3][1],dp[i][0]+k)
print(min(dp[N][0],dp[N][1]))