# src: https://www.acmicpc.net/problem/8723
L=list(map(int,input().split()))
L.sort()
if len(set(L))==1:
    print(2)
elif L[-1]**2==L[0]**2+L[1]**2:
    print(1)
else:
    print(0)
