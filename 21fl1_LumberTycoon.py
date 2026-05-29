import sys
sys.stdin=open("input.txt")
# → ↗ ↑ ↖ ← ↙ ↓ ↘
dy=[0,-1,-1,-1,0,1,1,1]
dx=[1,1,0,-1,-1,-1,0,1]
def is_valid(y,x):
    return 0<=y<n and 0<=x<n
def move_fertilzer(head,step):
    global F
    new_F=[]
    while F:
        cy,cx=F.pop()
        ny,nx=(cy+dy[head]*step)%n,(cx+dx[head]*step)%n
        new_F.append((ny,nx))
    F=new_F
def grow_tree():
    dy,dx=[-1,-1,1,1],[-1,1,1,-1]
    Cnt=[]
    for f in F:
        fy,fx=f
        A[fy][fx]+=1
    for f in F:
        fy,fx=f
        cnt=0
        for d in range(4):
            ny,nx=fy+dy[d],fx+dx[d]
            if is_valid(ny,nx) and A[ny][nx]>0:
                cnt+=1
        Cnt.append(cnt)
    for i in range(len(F)):
        fy,fx=F[i]
        A[fy][fx]+=Cnt[i]

def buy_fertilzer():
    global F
    new_F=[]
    for r in range(n):
        for c in range(n):
            if (r,c) not in F and A[r][c]>1:
                A[r][c]-=2
                new_F.append((r,c))
    F=new_F

n,m=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
F=[(n-2,0),(n-2,1),(n-1,0),(n-1,1)]
for _ in range(m):
    d,step=map(int,input().split())
    move_fertilzer(d-1,step)
    grow_tree() # cross +1 if tree>0
    buy_fertilzer()


print(sum(sum(A,[])))