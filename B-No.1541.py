# src: https://www.acmicpc.net/problem/1541
A=input().split("-")
L=list(map(lambda x:list(map(int,x.split('+'))),A))

for i in range(len(L)):
    L[i]=sum(L[i])
R=L[0]
for i in range(1,len(L)):
    R-=L[i]
print(R)
