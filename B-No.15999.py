# 2021-07-03
# src: https://www.acmicpc.net/problem/15999
import sys

# Input
N,M=map(int,input().split())
board = [input() for _ in range(N)]

# Moving Coordinates(ESWN)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

# goal
count=0

# Search board
for i in range(N): # X
    for j in range(M): # Y
        for f in range(4): # ESWN
            nx = i+dx[f]
            ny = j+dy[f]
            # Fixed color board
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if board[i][j] != board[nx][ny]:
                    count+=1
                    break
# account
answer=1
for i in range(N*M-count):
    answer=answer*2 %1000000007
print(answer)