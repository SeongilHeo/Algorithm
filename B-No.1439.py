# src: https://www.acmicpc.net/problem/1439
L=list(input())
b=L[0]
count=0
for x in L[1:]:
    if L[0]!=x and b!=x:
        count+=1
    b=x
print(count)