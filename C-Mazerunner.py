# src: https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner/submissions?page=1&pageSize=20

def searchSquare(): # pivot_point, pivot_dist
    pivot_dist=99
    pivot_point=[n,n]

    for i in range(m):
        y,x=M[i]
        r_d=out[0]-y
        c_d=out[1]-x
        temp_dist=max(abs(r_d),abs(c_d))
        temp_point=[max(max(y,out[0])-temp_dist,0),max(max(x,out[1])-temp_dist,0)]

        if pivot_dist > temp_dist:
            pivot_dist=temp_dist
            pivot_point=temp_point
        elif pivot_dist == temp_dist:
            pivot_dist=temp_dist
            pivot_point=min(pivot_point,temp_point,key=lambda x:(x[0],x[1]))

    return pivot_point,pivot_dist

def rotateSquare(pivot, n):
    ret=[[0]*n for _ in range(n)]
    origin=[a[pivot[1]:pivot[1]+n] for a in A[pivot[0]:pivot[0]+n]]

    for i in range(m):
        oy,ox=M[i]
        y,x=oy-pivot[0],ox-pivot[1]
        if 0<=y<n and 0<=x<n:
            if origin[y][x]==0:
                origin[y][x]=[-(i+1)]
            else:
                origin[y][x].append(-(i+1))
    y=out[0]-pivot[0]
    x=out[1]-pivot[1]


    if origin[y][x]==0:
        origin[y][x]=[-99]
    else:
        origin[y][x].append(-99)

    for r in range(n):
        for c in range(n):
            ret[c][n-1-r] = origin[r][c]

    for j in range(n):
        for i in range(n):
            if type(ret[j][i])!=type(0):
                for idx in ret[j][i]:
                    if idx==-99:
                        out[0]=pivot[0]+j
                        out[1]=pivot[1]+i
                    else:
                        M[-idx-1]=[pivot[0]+j,pivot[1]+i]
                    A[pivot[0]+j][pivot[1]+i]=0
            else:
                A[pivot[0]+j][pivot[1]+i]=max(ret[j][i]-1,0)


def moveMan(idx):
    dy,dx=[-1,1,0,0],[0,0,-1,1]
    py,px=M[idx]

    for i in range(4):
        ny=py+dy[i]
        nx=px+dx[i]
        if 0<=ny<n and 0<=nx<n and A[ny][nx] <= 0:
            if abs(py-out[0])>=abs(ny-out[0]) and abs(px-out[1])>=abs(nx-out[1]):
                M[idx]=[ny,nx]
                return True


n,m,k=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
M=[list(map(lambda n:int(n)-1,input().split())) for _ in range(m)]
out=list(map(lambda n:int(n)-1,input().split()))
cnt=0

for ik in range(k):
    for i in range(m):
        if moveMan(i):
            cnt+=1

    for i in range(m-1,-1,-1):
        if M[i][0]==out[0] and M[i][1]==out[1]:
            M.pop(i)
            m-=1


    if not M:
        break
        
    pivot_point,pivot_dist=searchSquare()
    rotateSquare(pivot_point,pivot_dist+1)

print(cnt)
print(out[0]+1,out[1]+1)
