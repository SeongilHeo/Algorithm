# src: https://www.acmicpc.net/problem/1598
a,b=map(int,input().split())
a-=1
b-=1
x=abs(b//4-a//4)
y=abs(a%4-b%4)
print(x+y)