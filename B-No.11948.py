# src: https://www.acmicpc.net/problem/11948
L=list(int(input()) for _ in range(6))
sub=min(L[:4])+min(L[4:])
print(sum(L)-sub)