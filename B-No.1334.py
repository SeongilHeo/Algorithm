src: https://www.acmicpc.net/problem/1334
def oddP(left,center):
    return int(left+center+left[::-1])
def evenP(left):
    return int(left+left[::-1])
def nextN(Nn):
    return str(int(Nn)+1) 

s=input()
N=int(s)
n=len(s)
left=s[:n//2]
center=""
if N<9:
    r=N+1
elif N<11:
    r=11
else:
    if n%2:
        center=s[n//2]
    if center:
        r=oddP(left,center)
        if N>=r:
            ncenter=nextN(center)
            if len(ncenter)>len(center):
                ncenter="0"
                nleft=nextN(left)
                if len(nleft)>len(left):
                    r=evenP(nleft)
                else:
                    r=oddP(nleft,ncenter)
            else:
                r=oddP(left,ncenter)
    else:
        r=evenP(left)
        if N>=r:
            nleft=nextN(left)
            if len(nleft)>len(left):
                r=oddP(nleft[:-1],nleft[-1])
            else:
                r=evenP(nleft)
print(r)