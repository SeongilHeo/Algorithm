# https://www.hackerrank.com/challenges/journey-to-the-moon/pㅌroblem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    # Write your code here
    I=[-1]*n
    M=[]

    tc=0
    for ast in astronaut:
        if I[ast[0]]<0:
            if I[ast[1]]<0:
                I[ast[0]]=tc
                I[ast[1]]=tc
                tc+=1
            else:
                I[ast[0]]=I[ast[1]]
        else:
            if I[ast[1]]<0:
                I[ast[1]]=I[ast[0]]
            else:
                t1=max(I[ast[0]],I[ast[1]])
                t2=min(I[ast[0]],I[ast[1]])
                if t1!=t2:
                    M.append([t1,t2])

    T=[0]*tc
    for i in range(n):
        if I[i]<0:
            continue
        else:
            T[I[i]]+=1

    while M:
        a,b=M.pop()
        if T[a]<0 and T[b]<0:
            if -T[a]!=-T[b]:
                M.append([-T[a],-T[b]])
        elif T[a]<0:
            if -T[a]!=b:
                M.append([-T[a],b])
        elif T[b]<0:
            if -T[b]!=a:
                M.append([-T[b],a]) 
        else:
            T[a]+=T[b]
            T[b]=-a

    
    result=n*(n-1)/2
    for i in range(len(T)):
        if T[i]<0:
            continue
        result-=T[i]*(T[i]-1)/2

    return int(result)    # Write your code here
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '
')

    fptr.close()
