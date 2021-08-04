# src: https://www.acmicpc.net/problem/2231
N=int(input())
s=0
for x in range(1000000):
    if N==sum(map(int,str(x)))+x:
        print(x)
        s=1
        break
if s==0:
    print(0)