# src: https://www.acmicpc.net/problem/6763
limit=int(input())
now=int(input())
gap=now-limit
if gap>0:
    if 1<=gap<21:
        dollor=100
    elif 21<=gap<31:
        dollor=270
    else:
        dollor=500
    print("You are speeding and your fine is $%d."%(dollor))
else:
    print("Congratulations, you are within the speed limit!")