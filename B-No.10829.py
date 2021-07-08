# src: https://www.acmicpc.net/problem/10829
n=int(input())
def solution(x):
    if x==0:
        return 0
    return solution(x//2)*10+x%2
print(solution(n))