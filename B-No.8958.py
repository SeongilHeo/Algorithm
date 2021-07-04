# src: https://www.acmicpc.net/problem/8958
def count(l):
    temp=0
    total=0
    for i in l:
        if i=="O":
            temp+=1
        else:
            temp=0
        total+=temp
    return total

n=int(input())
for i in range(n):
    l=input()
    print(count(l))