# src: https://www.acmicpc.net/problem/13706
N=int(input())
s,m,e=0,0,N
while True:
    m=(s+e)//2
    t=m**2
    if t<N:
        s=m
    elif t>N:
        e=m
    else:
        print(m)
        break