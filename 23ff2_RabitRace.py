from collections import defaultdict
from heapq import heappop, heappush

class RabitRace:
    def __init__(self):
        self.n=1
        self.m=1

        self.p=0
        self.RabitScore = []
        self.RabitJumped = []
        self.RabitPoision=[]
        self.RabitsPid=defaultdict(int)
        self.RabitPower = []

    def initRace(self,n,m,p,*R): # 100
        self.n=n # 3
        self.m=m # 5

        self.p=p
        self.RabitScore=[0]*p # idx: j
        self.RabitJumped=[0]*p # idx: j
        self.RabitPoision=[(0,0) for _ in range(p)] # idx: (r, c)
        for i in range(p):
            self.RabitsPid[R[i*2]] = i # idx: pid
            self.RabitPower.append(R[i*2+1]) # idx: power

        self.total_sum=0

    def jumpRabit(self,origin_y,origin_x,power): # need to append jump poisition
        options=[]
        # 오른쪽
        y,x=origin_y,origin_x
        dis=power%(2*(self.m-1))
        if x+dis<self.m:
            nx=x+dis
        else:
            nx=abs(2*(self.m-1)-(x+dis))
        options.append((y+nx,y,nx))

        # 아래쪽
        y,x=origin_y,origin_x
        dis=power %(2*(self.n-1))
        if y+dis<self.n:
            ny=y+dis
        else:
            ny=abs(2*(self.n-1)-(y+dis))
        options.append((ny+x,ny,x))

        # 왼쪽
        y,x=origin_y,origin_x
        dis=power % (2*(self.m-1))
        if 0<x-dis:
            nx=x-dis
        else:
            nx=abs(x-dis)
            if self.m<=nx:
                nx=2*(self.m-1)-nx
        options.append((y+nx,y,nx))

        # 위쪽
        y,x=origin_y,origin_x
        dis=power %(2*(self.n-1))
        if 0<y-dis:
            ny=y-dis
        else:
            ny=abs(y-dis)
            if self.n<=ny:
                ny=2*(self.n-1)-ny
        options.append((ny+x,ny,x))
        options.sort()
        return options[-1]

    def progressRace(self,k,s): # 200
        jumped=set()

        alpha_Rabit=[]
        for pid,i in self.RabitsPid.items():
            jump = self.RabitJumped[i]
            r, c = self.RabitPoision[i]
            heappush(alpha_Rabit,(jump,r+c,r,c,pid,i))

        for ik in range(k):
            jump,sum,r,c,pid,idx=heappop(alpha_Rabit)
            power=self.RabitPower[idx]
            _, nr,nc=self.jumpRabit(r,c,power)
            self.RabitPoision[idx]=(nr,nc)
            self.RabitJumped[idx]+=1
            bonus_score=nr+nc+2
            self.RabitScore[idx]-=bonus_score
            self.total_sum+=bonus_score
            jumped.add(pid)
            heappush(alpha_Rabit,(jump+1,nr+nc,nr,nc,pid,idx))
        jumped_Rabit=[]
        for pid in jumped:
            i=self.RabitsPid[pid]
            r,c=self.RabitPoision[i]
            heappush(jumped_Rabit,(-r-c,-r,-c,-pid,i))
        idx=heappop(jumped_Rabit)[-1]
        self.RabitScore[idx]+=s

    def updateDist(self,pid,L): # 300
        idx=self.RabitsPid[pid]
        self.RabitPower[idx]*=L

    def finish(self,): # 400
        print(max(self.RabitScore)+self.total_sum)

Race=RabitRace()

q=int(input())
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0] == 100:
        Race.initRace(*query[1:])
    elif query[0] ==200:
        Race.progressRace(*query[1:])
    elif query[0] == 300:
        Race.updateDist(*query[1:])
    elif query[0] == 400:
        Race.finish()
