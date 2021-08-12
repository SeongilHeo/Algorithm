# src: https://www.acmicpc.net/problem/10768
a=int(input())
b=int(input())
if a*1000+b<2018:
    print("Before")
elif a*1000+b>2018:
    print('After')
else:
    print("Special")