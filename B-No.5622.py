# src: https://www.acmicpc.net/problem/5622
target=input()

L=[]
for i in range(2,10):
    if i==7 or i==9:
        L+=[i]
    L+=[i]*3
R=[chr(i) for i in range(65,91)]
A=dict([(c,i) for c,i in zip(R,L)])

result=len(target)
for c in target:
    result+=A[c]
print(result)