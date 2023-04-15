# src: https://www.acmicpc.net/problem/12851
N,K=map(int,input().split())
A=[0]*100001
H=[[N]]
for i in range (100001):
    temp=[]
    cnt= H[-1].count(K)
    if cnt:
        break
    for pos in H[-1]:
        for p in [pos-1,pos+1,pos*2]:
            if p>-1 and p<100001 and A[p]==0:
                temp.append(p)
    for t in temp:
        A[t]=1
    H.append(temp)
print(len(H)-1,cnt)