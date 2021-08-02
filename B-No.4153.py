# src: https://www.acmicpc.net/problem/4153
while True:
    l=list(map(int,input().split()))
    if l==[0,0,0]:
        break
    l.sort()
    print("right" if l[0]**2+l[1]**2==l[2]**2 else "wrong")