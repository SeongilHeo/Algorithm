# src: https://www.acmicpc.net/problem/2884
H,M=map(int,input().split())
m=M+60-45
H=H if m//60 else (H+24-1)%24
M=m%60
print(H,M)