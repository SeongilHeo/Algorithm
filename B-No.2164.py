# src: https://www.acmicpc.net/problem/2164
N=int(input())
L=list(range(1,N+1))
a=1
while len(L)>1:
    l=len(L)
    L=L[a::2]
    if l%2==0:
        a^=0
    else:
        a^=1 # 0¹ø »ì·Á
print(L[0])