# src: https://www.acmicpc.net/problem/1011
N=int(input())
for _ in range(N):
    x,y=map(int,input().split())
    dist=y-x
    D=int(dist**(1/2))
    if dist==D*D:
        print(2*D-1)
    elif dist>D*D and dist<=D*D+D:
        print(2*D)
    elif dist>D*D and dist<(D+1)*(D+1):
        print(2*D+1)
