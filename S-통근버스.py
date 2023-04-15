# src: https://softeer.ai/practice/info.do?idx=1&eid=654
import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
T = [[0]*N for _ in range(N-2)]
for i in range(len(A)-2):
    t=A[i]-1 #최대 가능한
    for j in range(len(A)):
        if t==0:
            break
        if i==j:
            continue
        if A[i]<A[j]:
            if i<j: #2번 선택
                T[i][j]=t
        else:
            t-=1

print(sum(map(lambda x:sum(x),T)))