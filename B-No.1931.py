# src: https://www.acmicpc.net/problem/1931
N=int(input())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))

A.sort(key=lambda x:(x[1],x[0]))
cnt=0
E=0
for s,e in A:
    if s>=E:
        cnt+=1
        E=e
print(cnt)
