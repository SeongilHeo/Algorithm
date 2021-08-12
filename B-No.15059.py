# src: https://www.acmicpc.net/problem/15059
a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
print(sum([x if x>0 else 0 for x in [d-a,e-b,f-c]]))
