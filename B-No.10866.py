# src: https://www.acmicpc.net/problem/10866
import sys
from collections import deque

n=int(sys.stdin.readline())
D=deque()

for _ in range(n):
    cmd=sys.stdin.readline().split()
    if cmd[0]=="push_front":
        D.appendleft(cmd[1])      
    elif cmd[0]=="push_back":
        D.append(cmd[1])
    elif cmd[0]=="pop_front":
        print(D.popleft() if D else -1)
    elif cmd[0]=="pop_back":
        print(D.pop() if D else -1)
    elif cmd[0]=="size":
        print(len(D))
    elif cmd[0]=="empty":
        print(0 if D else 1)
    elif cmd[0]=="front":
        print(D[0] if D else -1)
    elif cmd[0]=="back":
        print(D[-1] if D else -1)
    else:
        print("Error")
    