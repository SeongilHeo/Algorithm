# src: https://www.acmicpc.net/problem/1676
n=int(input())
A=1
for i in range(1,n+1):
    A*=i
A=str(A)[::-1]
r=0
for i in range(len(A)):
    if A[i]!="0":
        r=i
        break
print(r)