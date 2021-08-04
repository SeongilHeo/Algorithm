# src: https://www.acmicpc.net/problem/10816
n=int(input())
L=list(map(int,input().split()))
m=int(input())
C=list(map(int,input().split()))

D={x:0 for x in C}
for x in L:
    if x not in D.keys():
        continue
    D[x]+=1

for x in C:
    print(D[x],end=" ")