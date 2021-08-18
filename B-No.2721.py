# src: https://www.acmicpc.net/problem/2721
N=int(input())
def T(n):
    return (1+n)/2*n
for _ in range(N):
    n=int(input())
    r=0
    for i in range(1,n+1):
        r+=i*T(i+1)
    print(int(r))