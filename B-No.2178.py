# src: https://www.acmicpc.net/problem/2178
N,M=map(int,input().split())
B=[list(map(int,list(input()))) for _ in range(N)]

dy,dx=[0,1,0,-1],[1,0,-1,0]

V=[0]*(N*M)
V[0]=1
q=[(0,0,V[0])]

while q:
    y,x,d=q.pop(0)
    if y==N and x==M:
        break
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<N and 0<=nx<M and V[ny*M+nx]==0:
            if B[ny][nx]==1:
                q.append((ny,nx,d+1))
                V[ny*M+nx]=d+1
print(V[N*M-1])