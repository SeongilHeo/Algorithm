# src: https://www.acmicpc.net/problem/2875
n,m,k=map(int,input().split())
team=n//2
team=min(team,m)
w_spare=n-team*2
m_spare=m-team
k-=w_spare+m_spare
while k>0:
    team-=1
    k-=3
print(team)