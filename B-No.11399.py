 src: https://www.acmicpc.net/problem/11399
N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
R=[x*(i+1) for i,x in enumerate(A)]
print(sum(R))