 src: https://www.codetree.ai/training-field/frequent-problems/destroy-the-turret

global alive, board,M,N
dx=[1,0,-1,0] # M
dy=[0,1,0,-1] # N   # 우하좌상

def updateAlive():
    for i in range(len(alive)-1,-1,-1):
        if alive[i][0]!=board[alive[i][2]][alive[i][3]]:
            alive[i][0]=board[alive[i][2]][alive[i][3]]
        if alive[i][0]<1:
            alive.pop(i)

    alive.sort(key = lambda x: (x[0],-x[1],-(x[2]+x[3]),-x[3]))

def findRoute(attacker,victim):
    
    Ar,Ac=attacker[2:4]
    Vr,Vc=victim[2:4]
    
    visited=[[False]*M for _ in range(N)]
    visited[Ar][Ac]=True
    
    q=deque()
    q.append([Ar,Ac])

    route=[]
    for j in range(N):
        temp=[]
        for i in range(M):
            temp.append([])
        route.append(temp)

    while q and not visited[Vr][Vc]:
        y,x=q.popleft()
        for i in range(4):
            ny=(y+dy[i])%N
            nx=(x+dx[i])%M
            if not visited[ny][nx] and board[ny][nx] != 0:
                visited[ny][nx]=True
                q.append([ny,nx])
                route[ny][nx]=route[y][x]+[[y,x]]

    return route[Vr][Vc]

    

def raserAttack(attacker,victim):
    route=findRoute(attacker,victim)
    if len(route)<1:
        return
    
    board[victim[2]][victim[3]]= max(board[victim[2]][victim[3]]-attacker[0],0)

    for ry,rx in route[1:]:
        board[ry][rx]= max(board[ry][rx]-attacker[0]//2,0)

    return route

def bombAttack(attacker,victim):
    r8=[-1,-1,-1,0,1,1,1,0]
    c8=[-1,0,1,1,1,0,-1,-1]
    Ar,Ac=attacker[2],attacker[3]
    Vr,Vc=victim[2],victim[3]
    damaged=[]
    board[Vr][Vc]=max(board[Vr][Vc]-attacker[0],0)

    for i in range(8):
        nr = (Vr+r8[i])%N
        nc = (Vc+c8[i])%M
        if board[nr][nc] > 0 and not (nr==Ar and nc==Ac):
            board[nr][nc]= max(board[nr][nc]-attacker[0]//2,0)
            damaged.append([nr,nc])

    return damaged

def growCannon(damaged):
    for i in range(1,len(alive)-1):
        if [alive[i][2],alive[i][3]] in damaged:
            continue
        else:
            board[alive[i][2]][alive[i][3]]+=1

def turn(time):
    alive[0][0]+=(N+M)
    alive[0][1]=time
    attacker=alive[0]
    
    board[attacker[2]][attacker[3]]+=(N+M)

    victim=alive[-1]

    damaged=raserAttack(attacker,victim)
    if not damaged:
        damaged=bombAttack(attacker,victim)

    growCannon(damaged)    

#r,c : y,x : N,M
N,M,K=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]

alive=[] # p,t,y,x
for i in range(N):
    for j in range(M):
        alive.append([board[i][j],0,i,j])
        
updateAlive()
for i in range(K):
    turn(i+1)
    updateAlive()
    if len(alive)==1:
        break

print(alive[-1][0])        