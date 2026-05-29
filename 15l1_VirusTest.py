import sys
sys.stdin=open("input.txt")
n=int(input())
client=list(map(int,input().split()))
leader,member=map(int,input().split())
ans=0
for i in range(n):
    client[i]-=leader
    ans += 1
    if client[i]<0:
        continue
    ans+=client[i]//member
    ans+=1 if client[i]%member else 0
print(ans)