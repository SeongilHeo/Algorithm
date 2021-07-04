# src: https://www.acmicpc.net/problem/1065
def check(x):
    if x<10:
        return True
    A=list(map(int,list(str(x))))
    d=A[0]-A[1]
    for i in range(1,len(A)-1):
        if d!=A[i]-A[i+1]:
            return False
    return True
n=int(input())
answer=0
for i in range(1,n+1):
    if check(i):
        answer+=1
print(answer)