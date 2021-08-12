# src: https://www.acmicpc.net/problem/16785
from math import *
a,b,c=map(int,input().split())

week=a*7+b # ¿œ¡÷¿œ coin

m=c//week
r=c%week

print(m*7+min(ceil(r/a),7))