# src: https://www.acmicpc.net/problem/21612
B=int(input())
r=5*B-400
print(r)
if r>B:
    print(-1)
elif r==B:
    print(0)
else:
    print(1)