# src: https://www.acmicpc.net/problem/21185
n=int(input())
if n%2==0:
    if n%4:
        print("Odd") 
    else:
        print("Even")
else:
    print("Either")