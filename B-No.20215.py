# src: https://www.acmicpc.net/problem/20215
w,h=map(int,input().split())
d=(w**2+h**2)**(1/2)
print(w+h-d)