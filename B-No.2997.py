# src: https://www.acmicpc.net/problem/2997
L=list(map(int,input().split()))
L.sort()
d1=L[1]-L[0]
d2=L[2]-L[1]
if d1==d2:
    print(L[2]+d1)
elif d1>d2:
    print((L[0]+L[1])//2)
else:
    print((L[2]+L[1])//2)
