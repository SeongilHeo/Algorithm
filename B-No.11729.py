# src: https://www.acmicpc.net/problem/11729
import sys
sys.setrecursionlimit(1000000)
def move(level,start,end):
    if level==1:
        print(start,end)
        return
    move(level-1,start,6-start-end)
    print(start,end)
    move(level-1,6-start-end,end)

N=int(input())
print(2**N-1)
move(N,1,3)