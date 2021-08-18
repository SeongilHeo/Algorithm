# src: https://www.acmicpc.net/problem/2566
x,y,r=-1,-1,0
for i in range(9):
    for j,dig in enumerate(map(int,input().split())):
        if r<dig:
            x,y,r=i,j,dig
            
print(r)
print(x+1,y+1)