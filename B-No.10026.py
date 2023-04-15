# src: https://www.acmicpc.net/problem/10026
n=int(input())
dy,dx=[0,1,0,-1],[1,0,-1,0]
B1=[]
B2=[]
for _ in range(n):
    B1.append(list(input()))
    B2.append(B1[-1][:])

R1=dict([("R",0),("G",0),("B",0)])
R2=dict([("R",0),("B",0)])
def solution(B,R,id):
    for i in range(n*n):
        r,c=i//n,i%n
        if B[r][c]==0:
            continue
        q=[(r,c)]
        if id==1:
            if B[r][c]=="B":
                target="B"
            else:
                target="R"
        else:
            target = B[r][c]
        R[target]+=1
        while q:
            y,x=q.pop(0)
            for i in range(4):
                ny=y+dy[i]
                nx=x+dx[i]
                if 0<=ny<n and 0<=nx<n:
                    if id==1:
                        if "B"==target:
                            if B[ny][nx]==target:
                                B[ny][nx]=0
                                q.append([ny,nx])
                        else:
                            if B[ny][nx]=="R" or B[ny][nx]=="G":
                                B[ny][nx]=0
                                q.append([ny,nx])
                    else:
                        if target==B[ny][nx]:
                            B[ny][nx]=0
                            q.append([ny,nx])
    return R
R1=solution(B1,R1,0)
R2=solution(B2,R2,1)
print(sum(R1.values()),sum(R2.values()))