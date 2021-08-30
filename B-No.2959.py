# src: https://www.acmicpc.net/problem/2959
l=list(map(int,input().split()))
l.sort()
print(min(l[2:])*min(l[:2]))