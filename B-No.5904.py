# src: https://www.acmicpc.net/problem/5904
def solution(size,recur):
    global n
    if n==1 or n==size+1:
        print('m')
        return
    elif n<=3 or n<=size+(recur+1)+3:
        print('o')
        return
    elif n<=size+(recur+1)+3+size:
        n-=(size+recur+4)
        solution(3,0)
        return
    recur+=1
    solution(2*size+recur+3,recur)

n=int(input())
solution(3,0)