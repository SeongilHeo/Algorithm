# src: https://school.programmers.co.kr/learn/courses/30/lessons/154539?language=python3
def solution(numbers):
    N=len(numbers)
    S=[(0,numbers[0])]
    answers=[-1]*N
    for i in range(1,N):
        while True:
            if S and S[-1][1] < numbers[i]:
                idx,num = S.pop()
                answers[idx]=numbers[i]
            else:
                S.append((i,numbers[i]))
                break
    return answers