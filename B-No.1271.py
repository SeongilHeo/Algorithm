# src: https://www.acmicpc.net/problem/1271
S=list(input())

h=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
H={x:i for i,x in enumerate(h)}

R=0
for i, dig in enumerate(S[::-1]):
    R+=H[dig]*16**i
print(R)