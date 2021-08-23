# src: https://www.acmicpc.net/problem/14397
import sys
input=sys.stdin.readline
r,c=map(int,input().split())
A=[[' ']*(2*c) for _ in range(r)]
for j in range(r):    
    for i, x in enumerate(input().strip()):
        A[j][i*2+j%2]=x
        

count=0
for i in range(r):
    for j in range(i%2,2*c,2):
        
        if j<2*c-2 and A[i][j]!=A[i][j+2]:
            count+=1
            
        if i!=0:
            if j!=0 and A[i][j]!=A[i-1][j-1]:
                count+=1
            if j<=2*c-2 and A[i][j]!=A[i-1][j+1]:
                count+=1            

                
print(count)
        