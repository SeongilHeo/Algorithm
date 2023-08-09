src: https://softeer.ai/practice/info.do?idx=1&eid=531
import sys
input=sys.stdin.readline

def dfs(color,left,right,bottom,top):
    global minArea
    for x,y in C[color]:
        new_left,new_right = min(left,x),max(right,x)
        new_bottom,new_top = min(y,bottom),max(y,top)
        area = (new_right-new_left)*(new_top-new_bottom)
        if minArea > area:
            if color == K:
                minArea=area
            else:
                dfs(color+1,new_left,new_right,new_bottom,new_top)
    return



        
N,K=map(int,input().split())
C=[[] for _ in range(K+1)]
for _ in range(N):
    x,y,color = map(int,input().split())
    C[color].append([x,y])

minArea = 2000*2000
dfs(1,1000,-1000,1000,-1000)
print(minArea)