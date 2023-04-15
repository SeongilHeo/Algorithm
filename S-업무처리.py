# src: https://softeer.ai/practice/info.do?idx=1&eid=1256
from math import log2 

H,K,R = map(int,input().split())
A=[]
for i in range(2**H):
    A.append(list(map(int,input().split())))

T = [[i] for i in range(2**(H+1))]
side=1
for n in range(2**H-1,0,-1):
    if side ==-1:
        T[n]=sum(map(list,zip(T[2*n],T[2*n+1])),[])
    else:
        T[n]=sum(map(list,zip(T[2*n+1],T[2*n])),[])
    if log2(n)%1==0:
        side*=-1
i=0
result=0
for d in range(R-H):
    if len(A[T[1][i%(2**H)]-2**H]):
        result+=A[T[1][i%(2**H)]-2**H].pop(0)
    i+=1

print(result)