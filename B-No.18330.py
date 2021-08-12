# src: https://www.acmicpc.net/problem/18330
a=int(input())
b=int(input())
b+=60
if a > b:
    print(3000*(a-b)+1500*b)
else:
    print(a*1500)