# src: https://www.acmicpc.net/problem/2470
N=int(input())
L=list(map(int,input().split()))
L.sort()
if L[-1]<0:
    print(L[-2],L[-1])
elif L[0]>0:
    print(L[0],L[1])
else: 
    a,b=0,len(L)-1
    M=[0,0,10**9]
    while a<b:
        t = L[a]+L[b]
        if abs(t)<M[2]:
            M=L[a],L[b],abs(t)
        if t>0:
            b-=1
        elif t<0:
            a+=1
        else:
            break
    print(M[0],M[1])