# src: https://www.acmicpc.net/problem/11866
n,k=map(int,input().split())
L=list(range(1,n+1))
i=1
j=0
Q=[]
while L:
    j=j%len(L)
    if i%k==0:
        Q.append(L.pop(j))
        j-=1
    i+=1
    j+=1
print("<"+", ".join(map(str,Q))+">")