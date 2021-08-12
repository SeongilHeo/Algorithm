# src: https://www.acmicpc.net/problem/17903
n, c=map(int,input().split())

R=1
for _ in range(n):
    l=list(map(int,input().split()))
    r=0
    for x in l:
        r= r or (0 if x<0 else 1)
    R = R and r

if R==0:
    print("unsatisfactory")
else:
    print("satisfactory")