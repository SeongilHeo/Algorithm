# src: https://school.programmers.co.kr/learn/courses/30/lessons/152995
def solution(scores):
    N = len(scores)
    answer=1
    
    a,b=scores[0]
    A=sorted(scores,key=lambda x:(x[0],-x[1]),reverse=True)
    bMax=-1
    for i in range(N):
        if a<A[i][0] and b<A[i][1]:
            return -1
        tempSum=sum(A[i])
        if a+b < tempSum:
            if bMax <= A[i][1]:
                bMax=max(bMax,A[i][1])
                answer+=1
    return answer