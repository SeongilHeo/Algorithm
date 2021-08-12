# https://www.acmicpc.net/problem/16199
by,bm,bd=map(int,input().split())
y,m,d=map(int,input().split())
r=y-by
if m<bm:
    r-=1
elif bm==m:
    if d<bd:
        r-=1
print(r)
print(y-by+1)
print(y-by)