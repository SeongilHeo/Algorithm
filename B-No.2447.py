# 2021-07-03
# src: https://www.acmicpc.net/problem/2447
def star(i,j,n):
    if ((i//n)%3 == 1) and ((j//n)%3 == 1):
        result[i][j]=' '
    else:
        if n==1:
            return
        else:
            star(i,j,n//3)
            
n=int(input())
result=[['*']*n for _ in range(n)]
for i in range(n//2+1):
    for j in range(n):
        star(i,j,n//3)

result[:n//2:-1]=result[:n//2]
for x in result:
    print(''.join(x))