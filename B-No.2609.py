# src: https://www.acmicpc.net/problem/2609
A,B=map(int,input().split())
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
G=gcd(A,B)
L=A*B//G
print(G)
print(L)