# src: https://www.acmicpc.net/problem/10101
a=int(input())
b=int(input())
c=int(input())
if a==b==c==60:
    print("Equilateral")
elif a+b+c==180 and len(set([a,b,c]))==2:
    print("Isosceles")
elif a+b+c==180 and len(set([a,b,c]))==3:
    print("Scalene")
elif a+b+c!=180:
    print("Error")