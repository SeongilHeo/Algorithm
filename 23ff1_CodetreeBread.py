from collections import deque
# number 3 - under
def search_home(r, c):
    path = deque([(r, c)])
    visited = [[False] * n for _ in range(n)]
    while path:
        cy, cx = path.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < n and 0 <= nx < n and A[ny][nx] < 2:
                if A[ny][nx] == 1:
                    return ny, nx
                if not visited[ny][nx]:
                    path.append((ny, nx))
                    visited[ny][nx] = True


def enterBase(t):  # number 3
    sy, sx = S[t]
    hy, hx = search_home(sy, sx)
    A[hy][hx] = 2
    Group_path[t] = (hy, hx)


def moveTo(t):  # number 1
    path = deque([(*Group_path[t], 0, 0)])
    visited = [[False] * n for _ in range(n)]
    cy, cx, _, _ = path.popleft()
    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]
        if 0 <= ny < n and 0 <= nx < n and A[ny][nx] < 2:
            if (ny, nx) == S[t]:  # find store at 1st rial
                return ny, nx
            if not visited[ny][nx]:
                path.append((ny, nx, 1, i))
                visited[ny][nx] = True

    mindist = n ** 2 + 1
    finded = False
    while path:
        cy, cx, dist, idx = path.popleft()
        if dist + 1 > mindist:
            continue
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < n and 0 <= nx < n and A[ny][nx] < 2:
                if (ny, nx) == S[t]:  # store find!!
                    Group_path[t] = Group_path[t][0] + dy[idx], Group_path[t][1] + dx[idx]
                    return
                if not visited[ny][nx]:
                    path.append((ny, nx, dist + 1, idx))
                    visited[ny][nx] = True


n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
S = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
Group_path = [(0, 0) for _ in range(m)]

dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]

t = 0
arrived = []
while len(arrived) < m:
    t += 1
    # numeber 1 - move
    B = []
    for i in range(min(t - 1, m)):
        if i in arrived:
            continue
        block = moveTo(i)  # arrived
        if block:
            arrived.append(i)
            B.append(block)

    # number 2 - block
    for by, bx in B:
        A[by][bx] = 2

    # number 3 - enter BaseCamp
    if t - 1 < m:
        enterBase(t - 1)

print(t)