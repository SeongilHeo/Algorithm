# src: https://www.acmicpc.net/problem/20233
a=int(input())
x=int(input())
b=int(input())
y=int(input())
m=int(input())
print(a+x*max((m-30),0)*21,b+y*max(m-45,0)*21)