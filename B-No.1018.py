# src: https://www.acmicpc.net/problem/1018
N,M=map(int,input().split())
board=[input() for _ in range(N)]

R=64
for sy in range(N-7):
    for sx in range(M-7):
        b,w=0,0
        for y in range(sy,sy+8):
            for x in range(sx,sx+8):
                if (x+y)%2==0: # 0,0 "w"
                    if board[y][x]=="B":
                        b+=1
                    elif board[y][x]=="W":
                        w+=1
                else: #0
                    if board[y][x]=="W":
                        b+=1
                    elif board[y][x]=="B":
                        w+=1
        R=min(R,b,w)
print(R)