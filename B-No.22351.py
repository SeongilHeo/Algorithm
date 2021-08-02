# src: https://www.acmicpc.net/problem/22351
S=input()
def check(a,b):
    if len(S)==len("".join([str(i) for i in range(a,b+1)])):
        return True
    else:
        return False
    
if len(S)>1 and check(int(S[0]),int(S[-1])):
    print(S[0],S[-1]) # 1-1
elif len(S)>2 and check(int(S[0]),int(S[-2:])):
    print(S[0],S[-2:])# 1-2
elif len(S)>3 and check(int(S[0]),int(S[-3:])): # 1-3
    print(S[0],S[-3:])
elif len(S)>3 and check(int(S[:2]),int(S[-2:])):# 2-2
    print(S[:2],S[-2:])
elif len(S)>4 and check(int(S[:2]),int(S[-3:])):# 2-3
    print(S[:2],S[-3:])
elif len(S)>5 and check(int(S[:3]),int(S[-3:])):# 3-3
    print(S[:3],S[-3:])
else:
    print(S,S)
