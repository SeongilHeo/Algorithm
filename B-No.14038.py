# src: https://www.acmicpc.net/problem/14038
L=[input() for _ in range(6)]
n=L.count('W')
if n>4:
    print(1)
elif n>2:
    print(2)
elif n>0:
    print(3)
else:
    print(-1)