# src: https://www.acmicpc.net/problem/1284
a=input()
D=dict({(str(i),3) for i in range(10)})
D['1']=2
D['0']=4
while a!='0':
    r=1
    for x in list(a):
        r+=D[x]+1
    print(r)
    a=input()