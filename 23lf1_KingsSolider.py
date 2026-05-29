l, n, q = map(int, input().split())  # 4 3 3
L = [list(map(int, input().split())) for _ in range(l)]
ML = [['-'] * l for _ in range(l)]
M_pos = []
M_size = []
M_hp = []
M_damage = [0] * n
M_alive = [True] * n

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

pushed = set()
moved = set()


def check_movable(idx, head):
    if M_alive[idx] == False:
        return True
    cy, cx = M_pos[idx]
    ch, cw = M_size[idx]
    sy,sx=cy+dy[head],cx+dx[head]
    ey,ex=cy+dy[head]+ch,cx+dx[head]+cw#sy+ch,sx+cw
    for r in range(sy,ey):
        for c in range(sx,ex):
            if 0 <= r < l and 0 <= c < l and L[r][c] != 2:
                if ML[r][c]==idx:
                    continue
                elif ML[r][c]!='-' and ML[r][c] not in moved:
                    pushed.add(ML[r][c])
            else:
                return False
    while pushed:
        p=pushed.pop()
        if not check_movable(p, head):
            return False
        moved.add(p)
    return True


def get_damage(idx):
    cy, cx = M_pos[idx]
    ch, cw = M_size[idx]
    damage = 0
    for r in range(cy, cy + ch):
        for c in range(cx, cx + cw):
            if L[r][c] == 1:
                damage += 1
    return damage


def update_ML():
    global ML
    ML = [['-'] * l for _ in range(l)]
    for idx in range(n):
        if M_alive[idx]:
            cy, cx = M_pos[idx]
            ch, cw = M_size[idx]
            for r in range(cy, cy + ch):
                for c in range(cx, cx + cw):
                    ML[r][c] = idx


def move_man(idx, head):
    global ML, pushed
    pushed.clear()
    moved.clear()
    status = check_movable(idx, head)
    if not status:
        return
    for p in moved:
        cy, cx = M_pos[p]
        ny, nx = cy + dy[head], cx + dx[head]
        M_pos[p] = (ny, nx)

        M_damage[p] += get_damage(p)
        if M_hp[p] <= M_damage[p]:
            M_alive[p] = False
    cy, cx = M_pos[idx]
    ny, nx = cy + dy[head], cx + dx[head]

    M_pos[idx] = (ny, nx)
    update_ML()

for idx in range(n):
    r, c, h, w, k = map(int, input().split())
    M_pos.append((r - 1, c - 1))
    M_size.append((h, w))
    M_hp.append(k)
    for dh in range(r-1, r-1 + h):
        for dw in range(c-1, c-1 + w):
            ML[dh][dw] = idx

for _ in range(q):
    i, d = map(int, input().split())
    move_man(i - 1, d)
score = 0
for idx in range(n):
    if M_alive[idx]:
        score += M_damage[idx]
print(score)

