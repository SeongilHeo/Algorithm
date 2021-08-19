# src: https://www.acmicpc.net/problem/1975
def trans(n,k):
    r=0
    while n:
        if n%k:
            break
        n=n//k
        r+=1
    return r

n=int(input())
for _ in range(n):
    a=int(input())
    r=0
    for i in range(2,a+1):
        r+=trans(a,i)
    print(r)