# src: https://www.acmicpc.net/problem/15474
from math import ceil
a,b,c,d,e=map(int,input().split())

print(min(ceil(a/b)*c,ceil(a/d)*e))