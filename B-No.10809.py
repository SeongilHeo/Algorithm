# src: https://www.acmicpc.net/problem/10809
txt=list(input())
result=[-1]*26

for i, c in enumerate(txt):
    t=ord(c)-97
    if result[t]==-1:
        result[t]=i
print(" ".join(map(str,result)))
        
    