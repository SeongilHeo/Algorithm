# src: https://www.acmicpc.net/problem/18414
x,l,r=map(int,input().split())
m=(10000000,-1)
for i in range(l,r+1):
    if m[0] > abs(x-i):
        m=abs(x-i),i
print(m[1])