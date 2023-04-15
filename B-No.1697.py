# src: https://www.acmicpc.net/problem/1697
N,K=map(int,input().split())

solved=False
Q=[(N,0)]
V=[False]*100001
result=0
while not solved:
    n,cnt=Q.pop(0)
    if n<0 or n>100000 or V[n]:
        continue
    if n==K:
        solved=True
        result=cnt
    else:
        Q.append((n-1,cnt+1))
        Q.append((n+1,cnt+1))
        Q.append((n*2,cnt+1))
        V[n]=True
print(result)
