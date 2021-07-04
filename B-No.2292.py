# src: https://www.acmicpc.net/problem/2292
x=int(input())
m,n=x//6,x%6
q=(-1+ (1+8*m)**(1/2))/2
Q= q-1 if not q%1 and n in [0,1] else q
result=int(Q)+2
print(result)