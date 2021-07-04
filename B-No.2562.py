# src: https://www.acmicpc.net/problem/2562
M=0,0
for i in range(9):
    a=int(input())
    if a>M[1]:
        M=i+1,a
print(M[1])
print(M[0])