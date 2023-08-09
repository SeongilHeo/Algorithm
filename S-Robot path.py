# src: https://softeer.ai/practice/info.do?idx=1&eid=577&sw_prbl_sbms_sn=247683
H,W=map(int, input().split())
B=[list(input()) for _ in range(H)]

remain=-1
for i in range(H):
    for j in range(W):
        if B[i][j]=='#':
            remain+=1
R=[]
minDist=[25*25,0,0,0]
dy,dx=[1,0,-1,0],[0,-1,0,1] # d: 0v 1< 2^ 3>

def dfs(y,x,d,route,remain,sy,sx,sd,visited):
    global minDist,R
    if minDist[0] < len(route):
        return
    if remain<1:
        if minDist[0] > len(route):
            minDist=[len(route),sy,sx,sd]
            R=route
        return
        
    visited[y][x]+=1

    if 0<=y+2*dy[d]<H and 0<=x+2*dx[d]<W:
        if visited[y+dy[d]][x+dx[d]]<2 and visited[y+2*dy[d]][x+2*dx[d]]<2:
            if B[y+dy[d]][x+dx[d]]=='#' and B[y+2*dy[d]][x+2*dx[d]]=='#':
                visited[y+dy[d]][x+dx[d]]+=1
                dfs(y+2*dy[d],x+2*dx[d],d,route+['A'],remain-2,sy,sx,sd,visited)

    if visited[y][x]<2:
        dfs(y,x,(d+3)%4,route+['L'],remain,sy,sx,sd,visited) # L
        dfs(y,x,(d+1)%4,route+['R'],remain,sy,sx,sd,visited) # R


for j in range(H):
    for i in range(W):
        for d in range(4):
            if B[j][i] =='#':
                visited=[[0]*W for _ in range(H)]
                dfs(j,i,d,[],remain,j,i,d,visited)
a,b,d=minDist[1:]

print(a+1,b+1)
arr=['v','<','^','>']
print(arr[d])
print(''.join(R))