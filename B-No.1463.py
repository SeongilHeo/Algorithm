# src: https://www.acmicpc.net/problem/1463
n=int(input())
dp=[0]*(n+1)
for i in range(1,n+1):
    if i==1:
        continue
    t=[]
    if i%2==0:
        t.append(dp[i//2])
    if i%3==0:
        t.append(dp[i//3])
    t.append(dp[i-1])
    dp[i]=min(t)+1
print(dp[-1])