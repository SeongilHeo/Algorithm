# src: https://www.acmicpc.net/problem/18222
from math import log2
def func(N,s):
    if N<2:
        if s==1:
            print(N^1)
        else:
            print(N)
        return
    logn=int(log2(N))
    if 2**logn*1.5<=N:
        func(N-2**logn,s^1) # ¹Ý´ë·Î
    else:
        func(N-2**(logn-1),s^0)
    
N=int(input())
func(N-1,0)
    