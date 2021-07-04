# 2021-07-03
# src: https://www.acmicpc.net/problem/10828
import sys

class Stack:
    def __init__(self):
        self.s=[]
    def push(self, x):
        self.s.append(x)
    def pop(self):
        return self.s.pop() if self.s else -1
    def size(self):
        return len(self.s)
    def empty(self):
        return 0 if self.s else 1
    def top(self):
        return self.s[-1] if self.s else -1

s=Stack()
n = int(sys.stdin.readline())
for i in range(n):
    com = sys.stdin.readline().split()
    if com[0]=="push":
        s.push(com[1])
    elif com[0]=="top":
        print(s.top())
    elif com[0]=="size":
        print(s.size())
    elif com[0]=="empty":
        print(s.empty())
    elif com[0]=="pop":
        print(s.pop())
    else:
        print("Error command")
    