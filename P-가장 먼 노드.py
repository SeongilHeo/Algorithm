def solution(n, edge):
    metrix=[[] for i in range(n+1)]
    for node in edge:
        metrix[node[0]].append(node[1])
        metrix[node[1]].append(node[0])

    visited=[False for _ in range(n+1)]
    visited[1]=True
    queue=[1]
    distance=[0 for _ in range(n+1)]

    while queue:
        i=queue.pop(0)
        for j in metrix[i]:
            if False==visited[j]:
                visited[j]=True
                queue.append(j)
                distance[j]=distance[i]+1

    return distance.count(max(distance))