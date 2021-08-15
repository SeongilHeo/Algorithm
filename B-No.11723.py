# src: https://www.acmicpc.net/problem/11723
import sys
input=sys.stdin.readline
n=int(input())
S=0
for _ in range(n):
    cmd=input().strip().split()
    if cmd[0]=="all":
        S=1048575
    elif cmd[0]=="empty":
        S=0
    else:
        cmd[1]=int(cmd[1])-1
        if cmd[0]=="add":
            S=S|(2**cmd[1])
        elif cmd[0]=="remove":
            S=S&(1048575-2**cmd[1])
        elif cmd[0]=="check":
            if S&(2**cmd[1])==0:
                print(0)
            else:
                print(1)
        elif cmd[0]=="toggle":
            S^=(2**cmd[1])