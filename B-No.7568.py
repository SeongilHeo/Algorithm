# src: https://www.acmicpc.net/problemi/7568
import sys
input=sys.stdin.readline

n=int(input())
L=[list(map(int,input().split())) for i in range(n)]

C=[]
for i in range(n):
    c=1
    for j in range(n):
        if i==j:
            continue
        if L[i][0]<L[j][0] and L[i][1]<L[j][1]:
            c+=1
    C.append(c)
print(" ".join(map(str,C)))