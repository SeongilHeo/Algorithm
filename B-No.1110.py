# src: https://www.acmicpc.net/problem/1110
n=int(input())
x=[n]
while True:
    a,b=x[-1]//10,x[-1]%10
    x.append(b*10+(a+b)%10)
    if x[-1]==x[0]:
        break
print(len(x)-1)