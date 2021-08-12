# src: https://www.acmicpc.net/problem/8718
L,one=map(float,input().split())
cases=[7*one,3.5*one,one/4*7]
print(max([int(x)*1000 for x in cases if x<=L]))