# src: https://www.acmicpc.net/problem/2630
def check(cx,cy,n):
    s=board[cy][cx]
    for j in range(cy,cy+n):
        for i in range(cx,cx+n):
            if board[j][i]!=s:
                return False
    return True

def solution(x,y,N):
    global W,B

    if check(x,y,N):
        if board[y][x]==1:
            B+=1
        else:
            W+=1
    else:
        t=N//2
        solution(x,y,t)
        solution(x,y+t,t)
        solution(x+t,y,t)
        solution(x+t,y+t,t)
        

N=int(input())
board=[list(map(int,input().split())) for _ in range(N)]

W,B=0,0
solution(0,0,N)
print(W)
print(B)