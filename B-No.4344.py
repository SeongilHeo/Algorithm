# src: https://www.acmicpc.net/problem/4344
n=int(input())
L=[]
for i in range(n):
    L.append(list(map(int,input().split())))
    

for l in L:
    avg=sum(l[1:])/l[0]
    c=0
    for x in l[1:]:
        if x>avg:
            c+=1 
    print("{:.3f}%".format(c/l[0]*100))