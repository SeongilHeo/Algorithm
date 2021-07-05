# # src: https://www.acmicpc.net/problem/1978
N=int(input())
A=list(map(int,input().split()))
count=0
def IsPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True

for x in A:
    if IsPrime(x):
        count+=1
print(count)