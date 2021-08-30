# src: https://www.acmicpc.net/problem/2061
pq,k=map(int,input().split())
s=0
for i in range(2,k):
    if pq%i==0:
        s=i
        break
if s:
    print("BAD %d"%s)
else:
    print("GOOD")