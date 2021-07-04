# src: https://www.acmicpc.net/problem/2675
n=int(input())
for i in range(n):
    num,string=input().split()
    num=int(num)
    string=list(string)
    print("".join([c*num for c in string]))
    