# src: https://www.acmicpc.net/problem/4493
t=int(input())
D={"R S":1,"R P":2,"S R":2,"S P":1,"P R":1,"P S":2,"R R":0,"S S":0,"P P":0}
for _ in range(t):
    n=int(input())
    one,two=0,0
    for _ in range(n):
        k=D[input()]
        if k==1:
            one+=1
        elif k==2:
            two+=1
        else:
            pass
    if one>two:
        print("Player 1")
    elif one==two:
        print("TIE")
    else:
        print("Player 2")
