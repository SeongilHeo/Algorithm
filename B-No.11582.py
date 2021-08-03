# src: https://www.acmicpc.net/problem/11582
N=int(input())
L=list(map(int,input().split()))
k=int(input())

def msort(left,mid,right):
    R=[]
    i,j=left,mid+1
    while i<=mid and j<=right:
        if L[i]<=L[j]:
            R.append(L[i])
            i+=1
        else:
            R.append(L[j])
            j+=1
    if i!=mid+1:
        R+=L[i:mid+1]
    else:
        R+=L[j:right+1]
    L[left:right+1]=R
        
n=N
while n!=k and n>1:   
    n//=2
    for i in range(n):
        left,right=i*(N//n),(i+1)*(N//n)-1
        mid=(left+right)//2
        msort(left,mid,right)
    
print(" ".join(map(str,L)))