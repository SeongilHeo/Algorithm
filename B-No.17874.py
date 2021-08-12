# src: https://www.acmicpc.net/problem/17874
a,b,c=map(int,input().split())

print(max((a-b)*(a-c),b*c,(a-b)*c,b*(a-c))*4)