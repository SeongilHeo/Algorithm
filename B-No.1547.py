# src: https://www.acmicpc.net/problem/1547
n=int(input())
A=[list(map(int,input().split())) for _ in range(n)]
ball=1
for a,b in A:
    if a==ball:
        ball=b
    elif b==ball:
        ball=a
print(ball)