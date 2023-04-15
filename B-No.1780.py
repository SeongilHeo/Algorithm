# src: https://www.acmicpc.net/problem/1780
import sys
input=sys.stdin.readline

def check(sr,sc,k): # y, x
    pivot=A[sr][sc]
    for i in range(sr,sr+k):
        for j in range(sc,sc+k):
            if pivot!=A[i][j]:
                return False
    return True

def solve(r,c,k):
    global R
    if k<1:
        return

    if check(r,c,k):
        R[A[r][c]+1]+=1
        return
    else:
        t=k//3
        solve(r,c,k//3)
        solve(r,c+t,k//3)
        solve(r,c+t*2,k//3)

        solve(r+t,c,k//3)
        solve(r+t,c+t,k//3)
        solve(r+t,c+t*2,k//3)

        solve(r+t*2,c,k//3)
        solve(r+t*2,c+t,k//3)
        solve(r+t*2,c+t*2,k//3)

n=int(input())
A=[]
for _ in range(n):
    A.append(list(map(int,input().split())))

R=[0]*3 # -1,0,1
solve(0,0,n)

for i in range(3):
    print(R[i])