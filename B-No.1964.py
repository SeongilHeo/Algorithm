# src: https://www.acmicpc.net/problem/1964
N=int(input())
R=5
for i in range(1,N):
    print(R)
    R+=i+(i+2)*2
print(R%45678)