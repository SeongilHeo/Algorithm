# src: https://www.acmicpc.net/problem/1352
# ref : http://www.secmem.org/blog/2019/04/22/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4/
def dp(x,s):
    if cc[x][s]!= -1:
        return cc[x][s]
    if s==N and x==N:
        cc[x][s]=1
        return cc[x][s]
    cc[x][s]=0
    if x<s:
        cc[x][s]|=dp(x+1,s)
    if s+x+1<=N:
        cc[x][s]|=dp(x+1,s+x+1)
    return cc[x][s]
def dfs(x,s):
    global cnt
    if s==N and x==N:
        return
    if x<s and dp(x+1,s):        
        print(chr(65-pq.pop()),end='')
        dfs(x+1,s)
    else:
        for i in range(x):
            pq.insert(0,-cnt)
        print(chr(64+cnt+1),end='')
        cnt+=1
        dfs(x+1,s+x+1)
N=int(input())
cc=[[-1]*111 for _ in range(111)]
cnt=0
pq=[]
if dp(0,0):
    dfs(0,0)
else:
    print(-1)