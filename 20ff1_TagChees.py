from copy import deepcopy

dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]

D_pos = [(-1, -1) for _ in range(16)]
D_head = [0] * 16

t_pos = [0, 0]
t_head = -1

A = [[0] * 4 for _ in range(4)]

for y in range(4):
    L = list(map(int, input().split()))
    for x in range(3, -1, -1):
        head = L.pop() - 1
        idx = L.pop() - 1
        D_pos[idx] = (y, x)
        D_head[idx] = head

        A[y][x] = idx


def moveD(A, D_pos, D_head, tag):
    y, x = D_pos[tag]
    D_head[tag] = -1
    A[y][x] = -1
    for idx in range(16):
        cy, cx = D_pos[idx]
        chead = D_head[idx]
        if chead == -1:
            continue
        for i in range(8):
            nh = (chead + i) % 8
            ny, nx = cy + dy[nh], cx + dx[nh]
            if 0 <= ny < 4 and 0 <= nx < 4:
                if ny==y and nx==x:
                    continue
                if A[ny][nx] == -1:
                    # update
                    A[cy][cx] = -1
                    A[ny][nx] = idx
                    D_head[idx] = nh
                    D_pos[idx] = (ny, nx)
                else:
                    # switch
                    o_idx = A[ny][nx]
                    A[cy][cx] = o_idx
                    A[ny][nx] = idx
                    D_pos[o_idx] = (cy, cx)
                    D_pos[idx] = (ny, nx)
                    D_head[idx] = nh
                break
    return A, D_pos, D_head


def findTag(A, t_pos, t_head):
    # move
    tagged = []
    if t_head == -1:
        tagged.append(A[0][0])
    else:
        ty, tx = t_pos
        for i in range(1, 4):
            ny, nx = ty + dy[t_head] * i, tx + dx[t_head] * i
            if 0 <= ny < 4 and 0 <= nx < 4 and A[ny][nx]>=0:
                tagged.append(A[ny][nx])
    return tagged

Reward = 0

def backTrack(A, D_pos, D_head, t_pos, t_head, now_reward):
    global Reward
    tagged = findTag(A, t_pos, t_head)
    if not tagged:
        Reward = max(Reward, now_reward)
        return
    else:
        for tag in tagged:
            new_t_pos, new_t_head = D_pos[tag], D_head[tag]
            new_A, new_D_pos, new_D_head = moveD(deepcopy(A), deepcopy(D_pos), D_head[:], tag)
            new_reward = now_reward + tag + 1
            backTrack(new_A, new_D_pos, new_D_head, new_t_pos, new_t_head, new_reward)

backTrack(A, D_pos, D_head, t_pos, t_head, 0)
print(Reward)

