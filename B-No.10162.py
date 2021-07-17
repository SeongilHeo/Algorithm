# src: https://www.acmicpc.net/problem/10162
T=int(input())
A,B,C=5*60,1*60,10
def solution(T):
    a,b,c=0,0,0
    if T%10:
        return "-1"
    if T>=A:
        a=T//A
        T-=a*A
    if T>=B:
        b=T//B
        T-=b*B
    if T>=C:
        c=T//C
        T-=c*C
    return "%d %d %d"%(a,b,c)
print(solution(T))