# src: https://www.acmicpc.net/problem/19698
n,w,h,l=map(int,input().split())
m=(w//l)*(h//l)
print(min(m,n))