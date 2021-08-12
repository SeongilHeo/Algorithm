# src: https://www.acmicpc.net/problem/13985
L=list(input().split('+'))
b,c=map(int,L[1].split('='))
if int(L[0])+b==c:
    print("YES")
else:
    print("NO")