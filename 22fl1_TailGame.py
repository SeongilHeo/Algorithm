from collections import deque

def set_route(cy,cx,idx):
    A_group[cy][cx] = idx+1
    for i in range(4):
        ny,nx=cy+dy[i],cx+dx[i]
        if 0<=ny<n and 0<=nx<n and not visted[ny][nx] and A[ny][nx]>0:
            visted[ny][nx]=True
            Group_path[idx].append((ny,nx))
            if A[ny][nx]<4:
                Group_num[idx]+=1
            set_route(ny,nx,idx)

def set_head(idx):
    ly,lx=Group_path[idx][-1]
    if A[ly][lx] == 2:
        Group_path[idx].rotate(-1)
        Group_path[idx].reverse()
# ---------------------------------------------
def move_step(idx):
    Group_path[idx].rotate()

def update_A(idx):
    for i,pos in enumerate(Group_path[idx]):
        r,c=pos
        if i<Group_num[idx]:
            A[r][c]=-(i+1)
        else:
            A[r][c]=4
# ---------------------------------------------
def shoot(k):
    arrow=(k//n)%4 # >,ㅅ,<,v
    num=k%n
    ty,tx=-1,-1
    if arrow==0: # num, 0++
        for c in range(n):
            if A[num][c]<0:
                ty,tx=num,c
                break
    elif arrow==1: # n--,num
        for r in range(n-1,-1,-1):
            if A[r][num]<0:
                ty,tx=r,num
                break
    elif arrow==2: # num,n--
        for c in range(n-1,-1,-1):
            if A[n-num-1][c]<0:
                ty,tx=n-num-1,c
                break
    elif arrow==3: # num, n--
        for r in range(n):
            if A[r][n-num-1]<0:
                ty,tx=r,n-num-1
                break
    if ty==-1:
        return
    return A_group[ty][tx]-1,A[ty][tx]**2 # group idx

def reverse_team(idx):
    temp=deque()
    for i in range(Group_num[idx]):
        cy,cx=Group_path[idx].popleft()
        temp.append((cy, cx))
    Group_path[idx].reverse()
    while temp:
        Group_path[idx].appendleft(temp.popleft())
# ---------------------------------------------

n,m,k=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
A_group=[A[i][:] for i in range(n)]

dy,dx=[0,1,0,-1],[1,0,-1,0] # >,v,<,ㅅ
visted=[[False]*n for _ in range(n)]

Group_path=[]
Group_num=[1]*m
for r in range(n):
    for c in range(n):
        if A[r][c]==1:
            visted[r][c]=True
            Group_path.append(deque([(r,c)]))

for i in range(m):
    r,c=Group_path[i][0]
    set_route(r,c,i)

for i in range(m):
    set_head(i)
total_score=0

for r in range(k):
    # number 1
    for i in range(m):
        move_step(i)
        update_A(i)
    # number 2
    result=shoot(r)
    if result:
        target_idx, score=result
        total_score += score
        reverse_team(target_idx)
print(total_score)