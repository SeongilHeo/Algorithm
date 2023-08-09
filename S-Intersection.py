# src: https://softeer.ai/practice/info.do?idx=1&eid=803&sw_prbl_sbms_sn=247580

from collections import deque

N=int(input())

log=deque()
for i in range(1,N+1):
    t,d=input().split()
    log.append([i,int(t),ord(d)-65])

load=[deque() for _ in range(4)]
onLoad=0

R=[-1]*N

def loadCars(time):
    global onLoad
    while log:
        if log[0][1] == time:
            i,t,d=log.popleft()
            load[d].append([i,t])
            onLoad+=1
        else:
            break
        
def goCars(time):
    global onLoad
    passed = []
    blocked=0
    for d in range(4):
        if load[d]:
            check_d=(d+3)%4
            if load[check_d]: # right block
                blocked+=1
            else:
                passed.append(d)
    for p in passed:
        i,t=load[p].popleft()
        R[i-1]=time
        onLoad-=1

    if blocked>3:
        log.clear()
        onLoad=0

time=log[0][1]
while log or onLoad:
    loadCars(time)
    goCars(time)
    if onLoad:
        time+=1
    else:
        if log:
            time=log[0][1]    
for r in R:
    print(r)