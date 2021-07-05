# src: https://www.acmicpc.net/problem/10250
n=int(input())
for _ in range(n):
    H,W,N=map(int,input().split())
    X,Y=N//H,N%H
    if Y==0:
        Y=H
    else:
        X+=1
    print(Y*100+X)