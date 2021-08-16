# src: https://www.acmicpc.net/problem/2580
import sys
input=sys.stdin.readline

B=[list(map(int,input().split())) for _ in range(9)]
zeros=[(x,y) for x in range(9) for y in range(9) if B[x][y] == 0]
z_len=len(zeros)
finished = False

def check(x,y):
    nums=[]
    for i in range(9): # x√‡
        nums.append(B[x][i])
    for i in range(9): # y√‡
        nums.append(B[i][y])
    rx=x//3*3
    ry=y//3*3
    for i in  range(rx,rx+3):
        for j in range(ry,ry+3):
            nums.append(B[i][j])
    return set(range(1,10))-set(nums)

def sudoku(cur):
    global finished
    if finished == True :
        return
    if cur == z_len:
        for item in B:
            print(*item)
        finished = True
        return
    else:
        x,y = zeros[cur]
        for c in check(x,y):
            B[x][y] = c
            sudoku(cur+1)
            B[x][y] = 0
sudoku(0)