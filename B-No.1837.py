# src: https://www.acmicpc.net/problem/1837
pq,k=map(int,input().split())
s=0
for i in range(2,k):
    if pq%i==0:
        s=i
        break
if s==0:
    print("GOOD")
else:
    print("BAD %d"%s)
