# src: https://www.acmicpc.net/problem/9498
score=int(input())

rank=score//10
if rank>=9:
    print("A")
elif rank>=8:
    print("B")
elif rank>=7:
    print("C")
elif rank>=6:
    print("D")
else:
    print('F')