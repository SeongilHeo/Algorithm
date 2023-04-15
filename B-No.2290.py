# src: https://www.acmicpc.net/problem/2290
s,n=input().split()
s=int(s)
N=list(map(int,list(n)))

b=" "*(s+2)
w=" "+"-"*s+" "
rl=" "*(s+1)+"|"
ll="|"+" "*(s+1)
bl="|"+" "*(s)+"|"

U=[w,b,w,w,b,w,w,w,w,w]
UH=[bl,rl,rl,rl,bl,ll,ll,rl,bl,bl]
M=[b,b,w,w,w,w,w,b,w,w]
LH=[bl,rl,ll,rl,rl,rl,bl,rl,bl,rl]
D=[w,b,w,w,b,w,w,b,w,w]

u,uh,m,lh,d="","","","",""
for n in N:
    u+=U[n]+" "
    uh+=UH[n]+" "
    m+=M[n]+" "
    lh+=LH[n]+" "
    d+=D[n]+" "
print(u)
for _ in range(s):
    print(uh)
print(m)
for _ in range(s):
    print(lh)
print(d)