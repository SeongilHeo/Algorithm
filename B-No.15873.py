# src: https://www.acmicpc.net/problem/15873
a=int(input())
if a>1000:
    print(a//100+a%100)
elif a>99:
    if a%10==0:
        print(a//100+10)
    else:
        print(a%10+10)
else:
    print((a%10)+(a//10))