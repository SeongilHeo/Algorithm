# src: https://www.acmicpc.net/problem/2798
N,M=map(int,input().split())
L=list(map(int,input().split()))
def func():
    m=M
    for i in range(len(L)-2):
        for j in range(i+1,len(L)-1):
            for k in range(j+1,len(L)):
                t=M-(L[i]+L[j]+L[k])
                if t<0:
                    continue
                if t==0:
                    print(M)
                    return
                if t<m:
                    m=t
    print(M-m)
func()
