# src: https://www.acmicpc.net/problem/1009
n=int(input())
D={}
D[0]=[10]
D[1]=[1]
D[2]=[2,4,8,6]
D[3]=[3,9,7,1]
D[4]=[4,6]
D[5]=[5]
D[6]=[6]
D[7]=[7,9,3,1]
D[8]=[8,4,2,6]
D[9]=[9,1]
for _ in range(n):
    a,b=map(int,input().split())
    print(D[a%10][b%len(D[a%10])-1])