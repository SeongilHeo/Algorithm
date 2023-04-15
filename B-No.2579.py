# src: https://www.acmicpc.net/problem/2579
N=int(input())
A=[]
for _ in range(N):
    A.append(int(input()))
if N>1:
    dp=[[0,0] for _ in range(N)]
    dp[:2]=[[A[0],A[0]],[A[0]+A[1],A[1]]]
    for n in range(2,N):
        dp[n][0]=dp[n-1][1]+A[n]
        dp[n][1]=max(dp[n-2])+A[n]
    print(max(dp[-1]))
else:
    print(A[-1])
