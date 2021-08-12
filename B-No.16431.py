# src: https://www.acmicpc.net/problem/16431
bx,by=map(int,input().split())
dx,dy=map(int,input().split())
jx,jy=map(int,input().split())

tx,ty=abs(jx-bx), abs(jy-by)
a,b=min(tx,ty),max(tx,ty)
B=b
D=abs(jx-dx)+abs(jy-dy)


if B<D:
    print("bessie")
elif D<B:
    print("daisy")
else:
    print("tie")