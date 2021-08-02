# src: https://www.acmicpc.net/problem/1874
N=int(input())
L=[int(input()) for _ in range(N)]
L.reverse()
stage=list(range(1,N+1))
stage.reverse()
R=[]
stack=[]
while len(L):
    if stack and stack[-1]==L[-1]:
        stack.pop()
        R.append('-')
        L.pop()
    else:
        if len(stage)==0:
            R=["NO"]
            break
        stack.append(stage.pop())
        R.append('+')
for x in R:
    print(x)