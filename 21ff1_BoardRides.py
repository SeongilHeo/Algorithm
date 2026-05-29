import sys
sys.stdin=open('input.txt','r')
n=int(input())
M=[(-1,-1) for i in range(n**2)]
A=[['-']*n for _ in range(n)]
love=[]
dy,dx=[-1,0,1,0],[0,1,0,-1]
def is_valid(y,x):
    return 0<=y<n and 0<=x<n
def get_empty_cnt(cy,cx):
    cnt=0
    for d in range(4):
        ny, nx = cy + dy[d], cx + dx[d]
        if is_valid(ny, nx) and A[ny][nx] == '-':
            cnt+=1
    return cnt
def get_best_neigh(*O):
    option=dict()
    for o in O:
        if M[o]!=(-1,-1):
            my,mx=M[o]
            for d in range(4):
                ny,nx=my+dy[d],mx+dx[d]
                if is_valid(ny,nx) and A[ny][nx]=='-':
                    if option.get(ny*n+nx):
                        option[ny*n+nx]+=1
                    else:
                        option[ny*n+nx]=1
    return option
def get_best_priority(option):
    max_neigh=0
    max_pos=(n,n)
    max_empty=0
    for pos, neigh in option.items():
        if neigh>max_neigh:
            cy,cx=pos//n,pos%n
            max_pos=(cy,cx)
            max_empty=get_empty_cnt(cy,cx)
            max_neigh=neigh
        elif neigh==max_neigh:
            cy,cx=pos//n,pos%n
            cnt=get_empty_cnt(cy,cx)
            if max_empty<cnt:
                max_empty=cnt
                max_pos=(cy,cx)
            elif max_empty==cnt:
                if max_pos>(cy,cx):
                    max_pos = (cy, cx)
    return max_pos
def get_empty_space():
    max_cnt=-1
    max_pos=(1,1)
    for r in range(n):
        for c in range(n):
            if A[r][c] == '-':
                cnt=0
                for d in range(4):
                    ny,nx=r+dy[d],c+dx[d]
                    if is_valid(ny, nx) and A[ny][nx] == '-':
                        cnt+=1
                if max_cnt<cnt:
                    max_cnt=cnt
                    max_pos=(r,c)

    return max_pos



def put_man(m,o1,o2,o3,o4):
    best_neighs=get_best_neigh(o1, o2, o3, o4)
    if best_neighs:
        my,mx=get_best_priority(best_neighs)
    else:
        my,mx=get_empty_space()

    A[my][mx]=m
    M[m]=(my,mx)
def get_score():
    total_score=0
    s_table=[0,1,10,100,1000]
    for l in love:
        m=l[0]
        my,mx=M[m]
        cnt = 0
        for o in l[1:]:
            oy,ox=M[o]
            if (my-oy, mx-ox) in [(-1,0),(0,1),(1,0),(0,-1)]:
                cnt+=1
        total_score+=s_table[cnt]
    return total_score



while True:
    try:
        m,o1,o2,o3,o4 = map(lambda x: int(x)-1,input().split())
    except:
        break
    put_man(m, o1, o2, o3, o4)
    love.append((m, o1, o2, o3, o4))

score=get_score()
print(score)
