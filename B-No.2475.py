# src: https://www.acmicpc.net/problem/2475
print(sum([int(x)**2 for x in input().split()])%10)