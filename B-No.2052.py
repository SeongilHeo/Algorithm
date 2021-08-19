# src: https://www.acmicpc.net/problem/2052
n=int(input())
a="%.300f"%(1/2**n)
l=300+2
for i in range(l-1,1,-1):
    if a[i]!='0':
        l=i
        break
print(a[:l+1])