# src: https://www.acmicpc.net/problem/2839
N=int(input())
S5,R5 = N//5,N%5
while True:
    S3,R3 = R5//3,R5%3
    if R3 == 0: # ¼º°ø
        print(S3+S5)
        break
    S5-=1
    if S5<0 and R3!=0:
        print(-1)
        break
    R5+=5