# src: https://www.acmicpc.net/problem/9012
n=int(input())
L=[input() for _ in range(n)]
def check(l):
    s=[]
    for x in l:
        if x=='(':
            s.append(x)
        else:
            if len(s)<1:
                return False
            s.pop()
    if s:
        return False
    return True
for l in L:
    print("YES" if check(l) else "NO")