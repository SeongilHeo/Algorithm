# src: https://www.acmicpc.net/problem/14935
a,b,c=map(int,input().split(':'))
d,e,f=map(int,input().split(':'))

S=f-c+60
if S<60:
    e-=1
S%=60
M=e-b+60
if M<60:
    d-=1
M%=60
H=d-a+24
H%=24
print(H*60*60+M*60+S)