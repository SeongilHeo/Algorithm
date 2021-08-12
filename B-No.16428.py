# src: https://www.acmicpc.net/problem/16428
a,b=map(int,input().split())
if a==0:
    print(0)
    print(0)
elif a<0: # - -
    if b<0:
        print(a//b+1)
        print(a%b-b)
    else: # - +
        print(a//b)
        print(a%b)
else:
    if b<0: # + -
        print(a//b+1)
        print(a%b-b)
    else: # + +
        print(a//b)
        print(a%b)