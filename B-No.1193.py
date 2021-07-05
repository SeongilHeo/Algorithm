# src: https://www.acmicpc.net/problem/1193
n=int(input())
q = (-1+(1+8*n)**(1/2))/2
line = int(q+1 if q%1 else q)
crit = (line*line-line)/2+1
diff = n-crit
sum_cord = line+1
x = sum_cord-diff-1
y = sum_cord-x
if line%2==0:
    x,y=y,x
print("%d/%d"%(x,y))