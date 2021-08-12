# src: https://www.acmicpc.net/problem/20839
ta,tc,te=map(int,input().split())
score=list(map(int,input().split()))
half=0
for x in score:
    if x>=te:
        half+=1
if half<2:
    print("E")
else:
    half=0
    for x in score:
        if tc<=x:
            half+=1
    if half==2:
        print("D")
    elif half<2:
        print("E")
    else:
        half=0
        for x in score:
            if ta<=x:
                half+=1
        if half==2:
            print("B")
        elif half<2:
            print("C")
        else:
            print("A")
