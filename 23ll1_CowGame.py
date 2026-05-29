n, m, p, c, d = map(int, input().split())
A = [['-'] * n for _ in range(n)]

cow_pos = tuple(map(lambda x: int(x)-1, input().split()))
cow_head = 0

P_id_pos = [list(map(int, input().split())) for _ in range(p)]
P_head = [-1] * p
P_alive = [0] * p
P_score = [0] * p
P_size=p

dy, dx = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
dyp, dxp = [-1, 0, 1, 0], [0, 1, 0, -1]
def init():
    global P_id_pos, A
    # sort by person's index
    P_id_pos.sort()
    # num to index & set matrix
    for ip in range(p):
        _id, py, px = P_id_pos[ip]
        P_id_pos[ip] = (_id, py - 1, px - 1)
        A[py - 1][px-1] = ip


def check_crash(idx):
    # crashed by cow
    if idx=="cow":
        cow_y, cow_x = cow_pos
        if A[cow_y][cow_x] != "-": # is person
            idx = A[cow_y][cow_x]
            throw_person(idx, cow_head, c, c,True)
    # crashed by person
    else:
        _id, py, px = P_id_pos[idx]
        if (py, px) == cow_pos:
            head = (P_head[A[py][px]] + 4) % 8  # reverse direction
            throw_person(idx, head, d, d, True)


def move_person(idx):
    cow_y, cow_x = cow_pos
    _id, py, px = P_id_pos[idx]

    best_dist = (cow_y - py) ** 2 + (cow_x - px) ** 2 # init (origin distance)
    best_head = -1 # init (out of index)
    # find best direction (priority: ↑ → ↓ ←)
    for i in range(4):
        ny, nx = py + dyp[i], px + dxp[i]
        if 0 <= ny < n and 0 <= nx < n and A[ny][nx] == '-':
            n_dist = (cow_y - ny) ** 2 + (cow_x - nx) ** 2
            if best_dist > n_dist:
                best_dist=n_dist
                best_head = i
    # convert dyp,dxp -> dy,dx
    covert_head = [1, 3, 5, 7] # ↑ → ↓ ←
    # move person & update matrix
    if best_head != -1:
        ny, nx = py + dyp[best_head], px + dxp[best_head]
        A[py][px] = '-'
        A[ny][nx] = idx
        P_id_pos[idx] = (_id, ny, nx)
        P_head[idx] = covert_head[best_head]

def search_nearest_person():
    shortest_dist = 2 * (n ** 2) + 1 # worst distance
    shortest_pos = (-1, -1) # worst position (out of matrix)

    # compare distance from cow to person (lived or stuned)
    for ip in range(p):
        if P_alive[ip] < 0: # dead person
            continue
        _id, py, px = P_id_pos[ip]
        cow_y, cow_x = cow_pos
        dist = (py - cow_y) ** 2 + (px - cow_x) ** 2
        if dist < shortest_dist:
            shortest_dist = dist
            shortest_pos = (py, px)
        elif dist == shortest_dist and (py, px) > shortest_pos:
            shortest_pos = (py, px)
    return shortest_pos

def move_cow():
    global cow_pos,cow_head
    # search goal position (nearest person)
    gy, gx = search_nearest_person()  # goal

    # set cow's direction (toward goal)
    cow_y, cow_x = cow_pos
    if gy-cow_y<0: y_head=-1 # < 0 > -1, 0 ,1
    elif gy-cow_y==0: y_head=0 # < 0 > -1, 0 ,1
    else: y_head=1

    if gx-cow_x<0: x_head=-1 # < 0 > -1, 0 ,1
    elif gx-cow_x==0: x_head=0 # < 0 > -1, 0 ,1
    else: x_head=1

    # set cow's direction as Heading INDEX
    best_head = -1
    for i in range(8):
        if dy[i] == y_head and dx[i] == x_head:
            best_head = i

    # move cow
    ny, nx = cow_y + dy[best_head], cow_x + dx[best_head]
    cow_pos = (ny, nx)
    cow_head = best_head

def throw_person(idx, head, power, score,stun=False):  # 8
    global P_size
    P_score[idx] += score
    if stun:
        P_alive[idx] = 2
    _id, py, px = P_id_pos[idx]
    A[py][px] = '-'
    ny, nx = py + dy[head] * power, px + dx[head] * power
    if 0 <= ny < n and 0 <= nx < n:
        if A[ny][nx] != '-':  # empty
            throw_person(A[ny][nx], head, 1, 0)
        A[ny][nx] = idx
        P_id_pos[idx] = (_id, ny, nx)
    else: # kill person
        P_alive[idx] = -1
        P_id_pos[idx] = (_id, -1, -1)
        P_size-=1

# setup
init()
for im in range(m):
    # move cow
    move_cow()
    check_crash("cow")
    # move people
    for ip in range(p):
        if P_alive[ip] == 0:
            move_person(ip)
            check_crash(ip)
    # update people's status
    for ip in range(p):
        if P_alive[ip] == -1:  # dead
            continue
        elif P_alive[ip] == 0:
            P_score[ip] += 1
        else:
            P_alive[ip] -= 1
            P_score[ip] += 1
    # escape when all dead
    if P_size==0:
        break
print(" ".join(map(str,P_score)))