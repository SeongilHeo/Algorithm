# 7

# len(city) = n <= 100
# len(road) <= 1_000
# x1 <= x2, y1 <= y2
# 1 <= limit <= 1_000_000
# |x|, |y| <= 1_000_000_000

# Case 1
city = [[-1, 3], # x, y
        [ 7, 3],
        [ 1,-1],
        [-2, 6]]
road=[[-1,  7,  7, 7, 80], # x1, y1, x2, y2, limit
      [-3,  3,  9, 3, 45],
      [-2, -4, -2, 6, 60],
      [ 1, -4,  1, 8, 50],
      [ 5,  1,  5, 7, 70]]
result=[70, 50, 0] # 1->2, 1->3, 1->4 # 0: no limit

# Case 2
city = [[3, 5],
        [3, 3],
        [2, 1],
        [9, 1],
        [7,-1]]
road=[[3,-2,3,4,30],
      [5,1,9,1,29],
      [3,4,3,8,99],
      [1,1,5,1,99],
      [7,-3,7,5,99]
      ]
result=[0,30,29,29] # 1->2, 1->3, 1->4 # 0: no limit

# Code
no_limit=1_000_000+1
def split_xy(road):
    x_parallel = []
    y_parallel = []
    for r in road:
        x1,y1,x2,y2,_ = r
        if x1==x2:
            y_parallel.append(r)
        elif y1 == y2:
            x_parallel.append(r)
        else:
            print("[Error] in split_xy")
    return x_parallel, y_parallel

def solution(city, road):
    # find_node
    Node=[]
    # O(n)
    for x,y in city:    
        # city
        Node.append((x,y,no_limit))
    # O(k)
    x_parallel, y_parallel = split_xy(road)
    # O(k)
    for x_road in x_parallel:
        x1,y,x2,y,x_limit=x_road
        # start
        Node.append((x1,y, no_limit))
        # camera
        Node.append(((x1+x2)//2,y,x_limit))
        # end
        Node.append((x2,y,no_limit))
    # O(k)
    for y_road in y_parallel:
        x,y1,x,y2,y_limit=y_road
        # start
        Node.append((x,y1,no_limit))
        # camera
        Node.append((x,(y1+y2)//2,y_limit))
        # end
        Node.append((x,y2,no_limit))
    # O(k^2)
    for x_road in x_parallel:
        x1,y,x2,y,_=x_road
        for y_road in y_parallel:
            x,y1,x,y2,_=y_road
            # intersections
            if (x1 <= x <= x2) and (y1<= y<= y2):
                Node.append((x,y,no_limit))

    # build Graph
    Graph = {i:[] for i in range(len(Node))}
    for x1,y1,x2,y2,_ in road:
        if x1==x2: # y_parallel
            candidate = []
            for idx,n in enumerate(Node):
                x,y,limit = n
                if x==x1:
                    candidate.append((idx,x,y,limit))
            candidate.sort(key=lambda x:x[2])
            before=None
            while candidate:
                temp = candidate.pop()
                if temp[2]<y1 or y2<temp[2]:
                    if before:
                        break
                    before=None
                    continue
                if before:
                    tlimit = min(temp[-1], before[-1])
                    Graph[temp[0]].append((before[0],tlimit))
                    Graph[before[0]].append((temp[0],tlimit))
                before=temp
        elif y1==y2: # x_parallel
            candidate = []
            for idx,n in enumerate(Node):
                x,y,limit = n
                if y==y1:
                    candidate.append((idx,x,y,limit))
            candidate.sort(key=lambda x:x[1])
            before=None
            while candidate:
                temp = candidate.pop()
                if temp[1]<x1 or x2<temp[1]:
                    if before:
                        break
                    before=None
                    continue
                if before:
                    tlimit = min(temp[-1], before[-1])
                    Graph[temp[0]].append((before[0],tlimit))
                    Graph[before[0]].append((temp[0],tlimit))
                before=temp

    # search limit
    answer=[]
    for goal in range(1,len(city)):
        answer.append(search(Graph, 0, goal))
    return answer

import heapq

INF=no_limit
def search(G,start,goal):
    n = max(G.keys()) + 1
    best = [-1] * n
    best[start] = INF
    pq = [(-INF, start)]

    while pq:
        b, u = heapq.heappop(pq)
        b = -b
        if u == goal:
            return b if b != INF else 0
        if b < best[u]:
            continue

        for v, w in G[u]:
            nb = min(b, w)
            if nb > best[v]:
                best[v] = nb
                heapq.heappush(pq, (-nb, v))

    print("[Error] search")

result == solution(city, road)