# src: https://www.acmicpc.net/problem/18111
import sys
input=sys.stdin.readline

n,m,b=map(int,input().split())
board=[]
for _ in range(n):
    board+=map(int,input().split())
    

gap=[0]*257
for x in board:
    gap[x]+=1
H,T=-1,n*m*256*2
for h in range(min(board),max(board)+1):
    minus=sum([(h-i)*x for i,x in enumerate(gap[:h])]) # 채워 요
    plus=sum([i*x for i,x in enumerate(gap[h:])]) # 남는다
    
    t=minus+plus*2
    if plus+b>=minus and T>=t:
        T=t
        H=h
print(T,H)