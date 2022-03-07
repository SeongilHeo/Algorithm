# src: https://www.acmicpc.net/problem/10798
import sys
input=sys.stdin.readline
A=[]
for i in range(5):
    l=input()
    A.append(l+(15-len(l))*' ')

print(''.join(sum(zip(*A),())).replace(' ',''))