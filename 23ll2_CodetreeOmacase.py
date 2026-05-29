def calculate_ETO(time,p_idx):
    global s_cnt
    p_time,p_pos=P_pos[p_idx] # yet_pos - 상대적
    now_pos=get_related_pos(time,p_time,p_pos)

    worst_x = max(S_pos[p_idx], key=lambda x: (now_pos - x) % l)
    additional_time= (now_pos - worst_x) % l
    P_out_time[p_idx] = max(P_out_time[p_idx],time + additional_time)

    while S_pos[p_idx]:
        x=S_pos[p_idx].pop()
        additional_time = (now_pos - x) % l
        P_need[p_idx] -= 1
        P_existed[p_idx] -= 1
        if additional_time==0:
            s_cnt-=1
        else:
            waiting.append(additional_time+time)
def get_fixed_pos(time,pos):
    return (pos-(time-1)%l)%l

def get_related_pos(time,p_time,p_pos):
    return (p_pos-(time-p_time))%l # absolute


def create_p_data(name):
    global p_size
    if outed:
        p_idx=outed.pop()
    else:
        p_idx=p_size
        p_size+=1
        P_name.append("")
        P_need.append(0)
        P_existed.append(0)
        P_pos.append(-1)
        P_out_time.append(0)
        S_pos.append([])
    P_name[p_idx]=name
    P_idx[name]=p_idx
    return p_idx

def delete_p_data(p_idx):
    global p_cnt
    outed.append(p_idx)
    P_idx.pop(P_name[p_idx])
    P_name[p_idx]=""
    P_need[p_idx]=0
    P_existed[p_idx]=0
    P_pos[p_idx] = -1
    P_out_time[p_idx]=0
    p_cnt-=1
    S_pos[p_idx] = []
def make_sushi(time,pos,name):
    global s_cnt
    s_cnt+=1
    p_idx=P_idx.get(name)
    if p_idx is None: # existed
        p_idx = create_p_data(name)
    P_existed[p_idx] += 1
    pos = get_fixed_pos(time,pos)
    S_pos[p_idx].append(pos)
    if P_need[p_idx] > 0:
        calculate_ETO(time,p_idx)

def enter_person(time, pos, name, n):
    global p_cnt
    p_cnt+=1
    p_idx=P_idx.get(name)
    if p_idx is None:
        p_idx=create_p_data(name)
    P_need[p_idx]=n
    pos=get_fixed_pos(time,pos)
    P_pos[p_idx] = (time,pos)
    if P_existed[p_idx]>0:
        calculate_ETO(time, p_idx)
def check_stauts(time):
    global s_cnt

    for p_idx in range(len(P_out_time)):
        if 0<P_out_time[p_idx] <= time and P_need[p_idx]==0:
            delete_p_data(p_idx)

    waiting.sort(reverse=True)
    while waiting and waiting[-1]<=time:
        waiting.pop()
        s_cnt-=1

def take_photo(time):
    check_stauts(time)
    print(p_cnt, s_cnt)

P_idx=dict()
P_name=[]
P_need=[]
P_existed=[]
P_pos=[]
P_out_time=[]
p_size=0
p_cnt=0
S_pos=[]
s_cnt=0
outed=[]
l,q = map(int, input().split())
waiting=[]


for iq in range(q):
    query=list(input().split())

    if query[0] == '100':
        time,pos,name=query[1:]
        make_sushi(int(time),int(pos),name)
    elif query[0] == '200':
        time,pos,name,n=query[1:]
        enter_person(int(time),int(pos),name,int(n))
    elif query[0] == '300':
        time=query[1]
        take_photo(int(time))