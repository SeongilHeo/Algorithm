# src: https://www.acmicpc.net/problem/19602
s=int(input())
m=int(input())
l=int(input())
if s*1+2*m+3*l >=10:
    print("happy")
else:
    print("sad")