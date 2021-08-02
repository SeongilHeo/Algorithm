# src: https://www.acmicpc.net/problem/10870
def fibo(N):
    if N in [0,1]:
        return N
    return fibo(N-1)+fibo(N-2)
    
N=int(input())
print(fibo(N))