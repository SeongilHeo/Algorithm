# src: https://www.acmicpc.net/problem/13610
from math import ceil
b,c=map(int,input().split())
print(ceil(c/(c-b)))