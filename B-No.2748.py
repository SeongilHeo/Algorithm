# src: https://www.acmicpc.net/problem/2748
n=int(input())
L=[0,1]+[0]*(n-1)
for i in range(2,len(L)):
    L[i]=L[i-1]+L[i-2]
print(L[-1])