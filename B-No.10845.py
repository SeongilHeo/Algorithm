# src: https://www.acmicpc.net/problem/10845
import sys

class Queue:
    def __init__(self):
        self.q=[]
        self.s=0
        self.pose=0
    def push(self, x):
        self.q.append(x)
        self.s+=1
    def pop(self):
        if self.s>0:
            self.s-=1
            self.pose+=1
            return self.q[self.pose-1]
        return -1
    def size(self):
        return self.s
    def empty(self):
        return 0 if self.s else 1
    def front(self):
        return self.q[self.pose] if self.s else -1
    def back(self):
        return self.q[-1] if self.s else -1
q=Queue()
n = int(sys.stdin.readline())
for i in range(n):
    com = sys.stdin.readline().split()
    if com[0]=="push":
        q.push(com[1])
    elif com[0]=="pop":
        print(q.pop())
    elif com[0]=="size":
        print(q.size())
    elif com[0]=="empty":
        print(q.empty())
    elif com[0]=="front":
        print(q.front())
    elif com[0]=="back":
        print(q.back())
    else:
        print("Error command")