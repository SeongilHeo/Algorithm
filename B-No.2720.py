# src: https://www.acmicpc.net/problem/2720
import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    M=int(input())
    q,d,n,p=0,0,0,0
    while M>0:
        if M>=25:
            M-=25
            q+=1
        elif M>=10:
            M-=10
            d+=1
        elif M>=5:
            M-=5
            n+=1
        else:
            M-=1
            p+=1
    print(q,d,n,p)