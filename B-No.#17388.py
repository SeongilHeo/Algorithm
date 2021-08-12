# src: https://www.acmicpc.net/problem/#17388
L=[(i,int(x)) for i,x in enumerate(input().split())]
L.sort(key=lambda x:x[1])

school=['Soongsil','Korea','Hanyang']
if sum(list(zip(*L))[1])>99:
    print('OK')
else:
    print(school[L[0][0]])
