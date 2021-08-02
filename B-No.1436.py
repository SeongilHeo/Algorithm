# src: https://www.acmicpc.net/problem/1436
N=int(input())
i=665
while N>0:
    i+=1
    if "666" in str(i):
        N-=1
print(i)