# src: https://www.acmicpc.net/problem/2920
L=list(map(int,input().split()))
status=L[1]-L[0] # 1:a/-1:d
for i in range(len(L)-1):
    if status!=L[i+1]-L[i]:
        status=2
        break
if status==1:
    print("ascending")
elif status==-1:
    print("descending")
else:
    print("mixed")