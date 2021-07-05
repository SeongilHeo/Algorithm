# src: https://www.acmicpc.net/problem/2869
A,B,V=map(int,input().split())
V=V-A
day=V/(A-B)
day=int(day+2 if day%1 else day+1)
print(day)