# src: https://www.acmicpc.net/problem/3460
n=int(input())
for _ in range(n):
    for i,x in enumerate(bin(int(input()))[:1:-1]):
        if x=='1':
            print(i,end=' ')
    print()