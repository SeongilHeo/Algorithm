# 2021-02-27
def solution(N, number):
    A = [set([int(str(N)*i)]) for i in range(1,9)]

    for i in range(8):
        for j in range(i):
            for a in A[j]:
                for b in A[i-j-1]:
                    A[i].add(a+b)
                    A[i].add(a-b)
                    A[i].add(a*b)
                    if b:
                        A[i].add(a//b)
        if number in A[i]:
            return i+1
    return -1