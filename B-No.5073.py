# src: https://www.acmicpc.net/problem/5073
while True:
    l=input()
    if l=="0 0 0":
        break
    a,b,c=map(int,l.split())
    if max(a,b,c) >= a+b+c-max(a,b,c):
        print("Invalid")
    elif a==b==c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")    