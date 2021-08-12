# src: https://www.acmicpc.net/problem/16727
p1,s1=map(int,input().split())
s2,p2=map(int,input().split())
r=-1
R=['Persepolis','Esteghlal','Penalty']
if (p1+p2)==(s1+s2):
    if p2>s1:
        r=0
    elif p2==s1:
        r=2
    else:
        r=1
elif (p1+p2)>(s1+s2):
    r=0
else:
    r=1
print(R[r])
    
    