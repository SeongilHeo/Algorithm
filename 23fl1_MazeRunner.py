def searchSquare(): # pivot_point, pivot_dist
    pivot_dist=99
    pivot_point=[n,n]

    for i in range(m):
        y,x=Group_path[i]
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
        oy,ox=Group_path[i]
        y,x=oy-pivot[0],ox-pivot[1]
        if 0<=y<n and 0<=x<n:
            if origin[y][x]==0:
                origin[y][x]=[-(i+1)]
            else:
                origin[y][x].append(-(i+1))
    y=out[0]-pivot[0]
    x=out[1]-pivot[1]

    print(out[0],pivot[0])

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
                        Group_path[-idx - 1]=[pivot[0] + j, pivot[1] + i]
                    A[pivot[0]+j][pivot[1]+i]=0
            else:
                A[pivot[0]+j][pivot[1]+i]=max(ret[j][i]-1,0)


def moveMan(idx):
    dy,dx=[-1,1,0,0],[0,0,-1,1]
    py,px=Group_path[idx]

    for i in range(4):
        ny=py+dy[i]
        nx=px+dx[i]
        if 0<=ny<n and 0<=nx<n and A[ny][nx] <= 0:
            if abs(py-out[0])>=abs(ny-out[0]) and abs(px-out[1])>=abs(nx-out[1]):
                Group_path[idx]=[ny, nx]
                return True

Data1="""10 10 100
7 7 1 0 4 8 3 1 0 9
2 1 8 4 1 9 5 2 3 7
7 2 9 8 6 3 6 8 8 1
1 5 9 0 4 0 9 5 0 8
0 0 0 8 4 1 6 0 1 4
9 5 8 9 2 9 7 0 0 7
3 0 7 1 6 5 3 2 6 0
9 2 7 3 6 6 7 6 6 8
0 5 0 9 4 9 3 4 2 3
9 0 3 0 2 6 0 4 8 7
5 2
9 3
5 2
4 4
7 10
6 9
5 8
7 10
10 7
5 8
10 4
"""
INPUT=(x for x in Data1.split("\n"))
input=next

n,m,k=map(int,input(INPUT).split())
A=[list(map(int,input(INPUT).split())) for _ in range(n)]
Group_path=[list(map(lambda n: int(n) - 1, input(INPUT).split())) for _ in range(m)]
out=list(map(lambda n:int(n)-1,input(INPUT).split()))
cnt=0

for ik in range(k):
    for i in range(m):
        if moveMan(i):
            cnt+=1

    for i in range(m-1,-1,-1):
        if Group_path[i][0]==out[0] and Group_path[i][1]==out[1]:
            Group_path.pop(i)
            m-=1

    if not Group_path:
        break
    pivot_point,pivot_dist=searchSquare()
    rotateSquare(pivot_point,pivot_dist+1)

print(cnt)
print(out[0]+1,out[1]+1)


