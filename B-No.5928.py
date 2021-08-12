# src: https://www.acmicpc.net/problem/5928
D,H,M=map(int,input().split())
if D*1440+H*60+M<11*1440+11*60+11:
    print(-1)
else:
    M=M-11+60
    if M<60:
        H-=1
    M%=60
    H=H-11+24
    if H<24:
        D-=1
    H%=24
    D-=11
    print(D*24*60+H*60+M)
