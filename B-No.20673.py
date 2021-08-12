# src: https://www.acmicpc.net/problem/20673
p=int(input())
q=int(input())
if q>=30:
    print("Red")
elif q<=10 and p<=50:
    print("White")
else:
    print("Yellow")