# src: https://www.acmicpc.net/problem/15829
n=int(input())
S=input()

L=[chr(i) for i in range(97,97+26)]
D={c:i+1 for i,c in enumerate(L)}

print(sum([D[c]* 31**i for i,c in enumerate(S)])%1234567891)