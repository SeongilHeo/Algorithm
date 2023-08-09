# src: https://www.acmicpc.net/problem/5525
N=int(input())
M=int(input())
S=input()

i=0
r=0
cnt=0
while i<M-1:
    if S[i:i+3]=="IOI":
        cnt+=1
        i+=2
        if cnt == N:
            r+=1
            cnt-=1
    else:
        i+=1
        cnt=0
print(r)