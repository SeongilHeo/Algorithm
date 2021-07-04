# src: https://www.acmicpc.net/problem/1316
n=int(input())
count=0
def check(string):
    L=list(string)
    a=dict([(chr(i),False) for i in range(97,123)])
    before=''
    for c in L:
        if before==c:
            continue
        before=c
        if a[c]==False:
            a[c]=True
        else:
            return False
    return True
    
for _ in range(n):
    string=input()
    if check(string):
        count+=1
print(count)