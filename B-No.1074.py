# src: https://www.acmicpc.net/problem/1074
N,r,c=map(int,input().split())

def search(r,c,size,base):

    if size<1:
        return base

    fr=r//size
    fc=c//size

    r-=fr*size
    c-=fc*size
    base+=fr*size**2*2+fc*size**2

    return search(r,c,size//2,base)
print(search(r,c,2**(N-1),0))