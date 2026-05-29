from collections import defaultdict
from heapq import heappop, heappush
import sys

class CodeTree:
    def __init__(self):
        # Queue
        self.Queue = defaultdict(list)
        self.queue_size = 0
        
        # Judge & Free Judge
        self.Judging = []
        self.J = []
        self.judge_free = 0
        
        # Domain
        self.DomainIdx = defaultdict(int) #"google.com:0, ..."
        self.domain_size = 0

        self.DomainNum=[] #"{0:0|1|2, 1:0|1|2}, ..."
        self.DomainStatus=[] #"time, ..."

    def setJudge(self, n, first_url):  # 100
        # Set Domain
        base, o_num = first_url.split('/')
        num = int(o_num)
        self.DomainIdx[base] = self.domain_size
        domain_idx=self.domain_size
        self.DomainNum.append(defaultdict(int))
        self.DomainNum[domain_idx][num]=1

        self.DomainStatus.append(0)

        self.domain_size += 1

        # Set Judge
        self.judge_free = n
        self.J = list(range(n))
        self.Judging = [[0, (0, 0)] for _ in range(n)] #  [start_time, (base,num), ...]

        # Insert Queue
        self.queue_size += 1
        heappush(self.Queue[domain_idx],(1,0,num))

    def requestJudge(self, t, p, url):  # 200
        # check Judging
        base, o_num = url.split('/')
        num = int(o_num)
        d_IDX=self.DomainIdx.get(base)

        if d_IDX is None:
            self.DomainIdx[base] = self.domain_size
            self.DomainNum.append(defaultdict(int))
            self.DomainNum[-1][num] = 0
            self.DomainStatus.append(0)
            d_IDX=self.domain_size
            self.domain_size += 1
        if self.DomainNum[d_IDX][num]!=1:
            heappush(self.Queue[d_IDX], (p, t, num))
            self.DomainNum[d_IDX][num]=1
            self.queue_size+=1

    def tryJudge(self, t):  # 300
        if self.judge_free < 1:
            return
        best_priority,best_time,best_domain_idx=50_001,0,-1
        for domain_idx in range(self.domain_size):
            que=self.Queue[domain_idx]            # empty
            if not que: continue                  # check History
            if t < self.DomainStatus[domain_idx]: continue# check Judging
            current_priority,current_time,current_num=que[0]
            if current_priority < best_priority or (current_priority==best_priority and current_time < best_time):
                best_priority,best_time,best_domain_idx=current_priority,current_time,domain_idx
        if best_priority >50_000:
            return

        # alocate Judge
        best_priority,best_time,best_num=heappop(self.Queue[best_domain_idx])
        jid = heappop(self.J)
        self.Judging[jid] = (t, (best_domain_idx,best_num))
        self.judge_free -= 1
        # update Que-size & Domain Status
        self.DomainNum[best_domain_idx][best_num]=2 # Queue->Judge
        self.DomainStatus[best_domain_idx]=1_000_001
        self.queue_size -= 1

    def offJudge(self, t, jid):  # 400
        # Delte judge from Judging
        start_t, url= self.Judging[jid]
        if start_t==0:
            return
        baseIDX,num=url
        self.Judging[jid] = [0, (0, 0)]  # None
        self.judge_free += 1
        heappush(self.J, jid)

        # Insert History and Update Domain
        # self.History.append((start_t, t,url, jid))
        self.DomainStatus[baseIDX]=(t-start_t)*3+start_t
    def lookQueue(self, t):  # 500
        print(self.queue_size)
dir="./sample/"
file="input0.txt"
sys.stdin=open(dir+"input/"+file,'r')
# sys.stdout=open(dir+"output/"+file,'w')
input=sys.stdin.readline

System = CodeTree()

q = int(input())
for _ in range(q):
    command = input().split()
    if command[0] == "100":
        n = int(command[1])
        first_url = command[2]
        System.setJudge(n, first_url)
    elif command[0] == "200":
        t = int(command[1])
        p = int(command[2])
        url = command[3]
        System.requestJudge(t, p, url)
    elif command[0] == "300":
        t = int(command[1])
        System.tryJudge(t)
    elif command[0] == "400":
        t = int(command[1])
        jid = int(command[2])
        System.offJudge(t, jid-1)
    elif command[0] == "500":
        t = int(command[1])
        System.lookQueue(t)
    else:
        print("Error")
        break