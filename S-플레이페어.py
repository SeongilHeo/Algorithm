 src: https://softeer.ai/practice/info.do?idx=1&eid=804
origin=input()
keys=input()

def encodeOrigin(origin):
    pose=0
    encode=list(origin)
    while True:
        if len(encode) == pose+1:
            encode.append('X')
            break
        if len(encode) <= pose:
            break
        if encode[pose]==encode[pose+1]:
            if encode[pose]=='X':
                encode.insert(pose+1,'Q')# Q추가
            else:
                encode.insert(pose+1,'X')# X추가
        pose+=2
    return encode

def initTable(keys):
    alpha=[-1]*26
    alpha[ord('J')-65]=0
    pose=0
    for key in keys:
        idx=ord(key)-65
        if alpha[idx]<0:
            alpha[idx]=pose
            pose+=1

    for i in range(26):
        if alpha[i]<0:
            alpha[i]=pose
            pose+=1
    return alpha

def showTable(alpha):
    A=[[0]*5 for _ in range(5)]
    r,c=0,0
    for i in range(26):
        if i ==9:
            continue
        r,c=alpha[i]//5,alpha[i]%5
        A[r][c]=chr(i+65)
    return A

encode=encodeOrigin(origin)
alpha=initTable(keys)
A=showTable(alpha)
for i in range(0,len(encode),2):
    P1,P2=alpha[ord(encode[i])-65],alpha[ord(encode[i+1])-65]
    y1,x1=P1//5,P1%5
    y2,x2=P2//5,P2%5
    if y1==y2:
        newy1,newx1=y1,(x1+1)%5
        newy2,newx2=y2,(x2+1)%5
    elif x1==x2:
        newy1,newx1=(y1+1)%5,x1
        newy2,newx2=(y2+1)%5,x2
    else:
        newy1,newx1=y1,x2
        newy2,newx2=y2,x1
    print(A[newy1][newx1]+A[newy2][newx2],end="")