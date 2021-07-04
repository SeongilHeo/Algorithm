# src: https://www.acmicpc.net/problem/2577
a=int(input())
b=int(input())
c=int(input())

L=str(a*b*c)
for i in range(10):
    print(L.count(str(i)))