# src: https://www.acmicpc.net/problem/20956
N,M=map(int,input().split())
L=[(i,int(x)) for i,x in enumerate(input().split())]
L.sort(key=lambda x: (x[1],-x[0]))

side=-1 # left
R,T=[],[]
while len(R)<M:
    x=L.pop() if L else (-1,-1)
    
    if len(T)==0:
        T.append(x)
    else:
        if T[-1][1]==x[1]:
            T.append(x)
        else:
            if T[-1][1]%7==0:
                if side*(-1)**len(T)==1:
                    T.reverse()
                R.append(T[0][0]+1)
                k=-1
                for _ in range(len(T)-1):
                    R.append(T.pop(k)[0]+1)
                    k*=-1
            else:
                for i in T[::side*-1]:
                    R.append(i[0]+1)
            T=[x]
            
    if x[1]%7==0: # is mint
        side*=-1

for x in R[:M]:
    print(x)