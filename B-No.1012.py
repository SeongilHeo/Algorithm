# src: https://www.acmicpc.net/problem/1012
dy,dx=[0,-1,0,1],[1,0,-1,0] #-> v <- ^
T=int(input())
for _ in range(T):
    M,N,K=map(int, input().split())
    B=[[0]*M for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        B[y][x]=-1
    cnt=0
    for i in range(N*M):
        r,c=i//M,i%M
        if B[r][c]<0:
            cnt+=1
            B[r][c]=cnt
            q=[(r,c)]
            while q:
                y,x=q.pop(0)
                for i in range(4):
                    ny=y+dy[i]
                    nx=x+dx[i]
                    if 0<=ny<N and 0<=nx<M and B[ny][nx]<0:
                        q.append((ny,nx))
                        B[ny][nx]=cnt
    print(cnt)