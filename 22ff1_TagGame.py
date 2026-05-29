import sys
file="input.txt"
sys.stdin=open(file,'r')
n,m,h,k=map(int,input().split())
M=[list(map(lambda x: int(x)-1,input().split())) for _ in range(m)]
H=[list(map(lambda x: int(x)-1,input().split())) for _ in range(h)]
A=[[list() for _ in range(n)] for _ in range(n)]
one_pos=[n//2,n//2,3]
one_reamin=[1,1,1,1]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]  # > v < ㅅ
catched=[False]*m
ANS=0
def move_target(idx):
    global one_pos
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]  #>0,v1, <,ㅅ
    cy,cx,cd=M[idx]
    oy,ox,_=one_pos
    if abs(cy-oy)+abs(cx-ox) > 3:
        return
    ny,nx=cy+dy[cd],cx+dx[cd]
    if 0<=ny<n and 0<=nx<n:
        if ny==oy and nx==ox:
            return
        if A[ny][nx] !='t':
            A[ny][nx].append(idx)
        if A[cy][cx]!='t':
            A[cy][cx].remove(idx)
        M[idx] = (ny, nx, cd)

    else:
        if cd==2 or cd ==3:
            cd-=2
        else:
            cd+=2
        ny, nx = cy + dy[cd], cx + dx[cd]
        if ny == oy and nx == ox:
            return
        if A[ny][nx] != 't':
            A[ny][nx].append(idx)
            M[idx] = (ny, nx, cd)
        if A[cy][cx]!='t':
            A[cy][cx].remove(idx)
        M[idx] = (ny, nx, cd)

def move_one():
    global one_pos,one_reamin
    cy,cx,cd=one_pos
    ny,nx=cy+dy[cd],cx+dx[cd]
    if ny==0 and nx ==0:
        nd=1
        one_reamin=n-1,-1,2,n-1,
    elif ny==n//2 and nx ==n//2:
        nd=3
        one_reamin=1,1,1,1
    else:
        step,updown,trial,gap=one_reamin # 3 / 1 / 1
        new_gap=gap-1
        if new_gap==0:
            if trial==0:
                new_trial=1
                new_step=step+updown
            else:
                new_trial=trial-1
                new_step = step
            new_gap=new_step
            nd = (cd+updown)%4

        else:
            nd=cd
            new_step=step
            new_trial=trial
        one_reamin=[new_step,updown,new_trial,new_gap]

    one_pos=[ny,nx,nd]

def look_one():
    oy,ox,od=one_pos
    cnt=0
    for i in range(3):
        ny,nx=oy+i*dy[od],ox+i*dx[od]
        if 0<=ny<n and 0<=nx<n:
            if not A[ny][nx] or A[ny][nx] == 't':
                continue
            else:
                dead_idxs=A[ny][nx]
                for d in dead_idxs:
                    catched[d]=True
                    M[d]=(-1,-1,-1)
                    A[ny][nx]=list()
                    cnt+=1
    return cnt

for i in range(m):
    y,x,d=M[i]
    A[y][x].append(i)
for i in range(h):
    y,x=H[i]
    A[y][x]='t'

for ik in range(k):

    for im in range(m):
        if not catched[im]:
            move_target(im)

    move_one()
    cnt=look_one()
    ANS+=cnt*(ik+1)

print(ANS)