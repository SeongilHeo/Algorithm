# src: https://www.acmicpc.net/problem/14470
now,goal,tf,td,tnf=[int(input()) for _ in range(5)]
r=0
if now <0:
    r+=abs(now)*tf+td
    now=0
work=goal-now
r+=work*tnf
print(r)