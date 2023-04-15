# src: https://www.acmicpc.net/problem/9375
n=int(input())
for _ in range(n):
    t=int(input())
    A=dict()
    cnt=1
    for _ in range(t):
        name, kind =input().split()
        if not A.get(kind):
            A[kind]=2
        else:
            A[kind]+=1
    for x in A.values():
        cnt*=x
    print(cnt-1)

        