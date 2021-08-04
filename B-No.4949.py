# src: https://www.acmicpc.net/problem/4949
import sys
# input=sys.stdin.readline
def check(line):
    s=[]
    for c in line:
        if c=="(":
            s.append(c)
        elif c==")":
            if s and s[-1]=="(":
                s.pop()
            else:
                return False
        elif c=="[":
            s.append(c)
        elif c=="]":
            if s and s[-1]=="[":
                s.pop()
            else:
                return False
        else:
            pass
    if s:
        return False
    return True
        
        
while True:
    line=input()
    if "."==line:
        break
    print("yes" if check(line) else "no")