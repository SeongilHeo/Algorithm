# src: https://www.acmicpc.net/problem/3052
L=[int(input()) for _ in range(10)]
print(len(set(map(lambda x:x%42,L))))