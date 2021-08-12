# src: https://www.acmicpc.net/problem/14623
a=sum([2**i*int(b) for i,b in enumerate(input()[::-1])])
b=sum([2**i*int(b) for i,b in enumerate(input()[::-1])])
print(bin(a*b)[2:])