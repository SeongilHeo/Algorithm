# src: https://www.acmicpc.net/problem/4299
a,b=list(map(int,input().split()))
A,B=(a+b)/2,(a-b)/2
if A<B:
    A,B=B,A
if A%1 or B%1 or A<0 or B<0:
    print(-1)
else:
    print(int(A),int(B))