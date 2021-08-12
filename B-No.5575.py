# src: https://www.acmicpc.net/problem/5575
for _ in range(3):
    L=list(map(int,input().split()))
    s=L[5]-L[2]+60
    if s<60:
        L[4]-=1
    s%=60
    m=L[4]-L[1]+60
    if m<60:
        L[3]-=1
    m%=60
    h=L[3]-L[0]
    print(h,m,s)
