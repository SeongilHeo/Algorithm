# 현대오토에버 2023 3분기 신입 2번..
N=int(input(INPUT))
user_map={x:i for i,x in enumerate(input(INPUT).split())}
day_map={x:i for i,x in enumerate(['Mon','Tue','Wed','Thu','Fri'])}
users_times=[[[0]*54 for _ in range(5)] for _ in range(N)]

def checkTable(table,time):
    s,e=time
    for i in range(s,e):
        table[i]=1
    return table
def sumTable(table,user_table):
    for i in range(54):
        table[i]+=user_table[i]
    return table
def checkMaxFree(table):
    ans=0
    temp=0
    for i in range(54):
        if table[i]==0:
            temp+=1
        else:
            ans=max(ans,temp)
            temp=0
    return ans

M=int(input(INPUT))
for _ in range(M):
    d,a,b,x,y,s = input(INPUT).split()

    start_time=((int(a)*60+int(b)))//10-54
    end_time=(int(x)*60+int(y))//10-54

    day=day_map[d]
    users=[user_map[u] for u in s.split(',')]
    for u in users:
        table=users_times[u][day]

        table=checkTable(table,[start_time,end_time])

K=int(input(INPUT))
for _ in range(K):
    D,U=input(INPUT).split()
    days=[day_map[d] for d in D.split(',')]
    users=[user_map[u] for u in U.split(',')]
    answer=0
    for d in days:
        table=[0]*54
        for u in users:
            table=sumTable(table,users_times[u][d])
        answer=max(answer,checkMaxFree(table))
    print(answer*10)

"""3
a b c
10
Mon 10 0 11 0 a,b,c
Tue 10 0 11 0 a,b,c
Wed 10 0 11 0 a,b,c
Thu 10 0 11 0 a,b,c
Fri 10 0 11 0 a,b,c
Mon 14 0 15 30 a,b,c
Tue 14 0 15 0 a,b,c
Wed 12 0 13 30 b,c
Thu 16 10 18 0 a,b,c
Fri 15 0 17 20 a,c
4
Mon a,c
Tue a,b,c
Thu a,b,c
Fri b,c
""""