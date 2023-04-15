 # src: https://www.codetree.ai/training-field/frequent-problems/artistry
from collections import deque

global n, board, group,dx,dy, visited, groupPerm, artScore

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 북 남, 서, 동
dx = [-1,1,0,0]
dy = [0,0,-1,1]

artScore = 0

# 숫자 같은데 인접한 칸 계산
def bfs(i,j):
    q = deque()
    q.append([i,j])
    tmp = [[i,j]]
    color = board[i][j]
    visited[i][j] = True

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if board[nx][ny] == color:
                        visited[nx][ny] = True
                        q.append([nx,ny])
                        tmp.append([nx,ny])
    return tmp

# 인접한 그룹들의 좌표를 배열로 저장
def getGroups():
    groups = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                groups.append(bfs(i,j))
    return groups

# 모든 조합 계산
def perm(total):
    permList = []
    for i in range(total):
        for j in range(i+1,total):
            permList.append([i,j])
    return permList

# 인접한 쌍인지 판단(return>0) & 변의 개수(return) : 
def cntEdge(i,j):
    cnt=0
    for x,y in group[i]:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if [nx,ny] in group[j]:
                cnt+=1
    return cnt

# 예술성 계산
def cal():
    score = 0
    for i,j in groupPerm:
        e = cntEdge(i,j)
        if e:
            a = len(group[i])
            b = len(group[j])
            c = board[group[i][0][0]][group[i][0][1]]
            d = board[group[j][0][0]][group[j][0][1]]
            score += (a+b)*c*d*e
    return score

# 행렬 회전
def turnMatrix():
    newMatrix=[[0]*n for _ in range(n)]
    s,m,e=0,n//2,n
    for i in range(s,m):
        for j in range(s,m):
            newMatrix[i][j]=board[m-s-1-j][i]
    for i in range(s,m):
        for j in range(m+1,e):
            newMatrix[i][j]=board[e-j-1][i+m+1]
    for i in range(m+1,e):
        for j in range(s,m):
            newMatrix[i][j]=board[e-j-1][i-m-1]
    for i in range(m+1,e):
        for j in range(m+1,e):
            newMatrix[i][j]=board[e+m-j][i]  
    
    for i in range(n):
        newMatrix[i][n//2]=board[n//2][n-i-1]
        newMatrix[n//2][i]=board[i][n//2]

    return newMatrix        

cnt=4
while cnt:
    visited = [[False for _ in range(n)] for _ in range(n)]
    group = getGroups()
    groupPerm = perm(len(group))
    artScore += cal()
    board=turnMatrix()
    cnt-=1
print(artScore)