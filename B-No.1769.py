# src: https://www.acmicpc.net/problem/1769
N=input()
count=0

def solution(N):
    global count
    if len(N)==1:
        return N
    count+=1
    return solution(str(sum(list(map(int,N)))))

R= int(solution(N))
print(count)
print("NO" if R%3 else "YES")