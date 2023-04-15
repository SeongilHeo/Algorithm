# src: https://www.acmicpc.net/problem/2667
N=int(input())
B=[list(map(int,list(input()))) for _ in range(N)]

V=[[0]*N for _ in range(N)]
dy,dx=[0,1,0,-1],[1,0,-1,0]
R=[]
def dfs(r,c,deep):
    V[r][c]=1
    for i in range(4):
        nr=r+dy[i]
        nc=c+dx[i]
        if 0<=nr<N and 0<=nc<N and V[nr][nc]==0 and B[nr][nc]!=0:
            deep=dfs(nr,nc,deep+1)
    return deep


for j in range(N):
    for i in range(N):
        if B[j][i]!=0 and V[j][i]==0:
            r=dfs(j,i,1)
            R.append(r)
R.sort()
print(len(R))
for r in R:
    print(r)
