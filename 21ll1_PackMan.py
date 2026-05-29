import sys
sys.stdin=open("input.txt")
def is_valid(y, x):
    return 0 <= y < 4 and 0 <= x < 4

def try_duplication():
    for r in range(4):
        for c in range(4):
            for d in range(8):
                A_egg[r][c][d] = A[r][c][d]
def move_monster():
    global A
    dym = [-1,-1,0,1,1,1,0,-1]
    dxm = [0,-1,-1,-1,0,1,1,1]
    new_A = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            if sum(A[r][c])==0:
                continue
            poss = []
            for d in range(8):
                nr, nc = r + dym[d], c + dxm[d]
                if is_valid(nr, nc) and A_corpse[nr][nc] == 0 and (nr,nc)!=pac_pos:
                    poss.append(d)
            if poss:  # [1,2,3]
                for i in range(8):
                    if A[r][c][i]==0:
                        continue
                    if i in poss:
                        nr, nc = r + dym[i], c + dxm[i]
                        new_A[nr][nc][i] += A[r][c][i]
                    else:
                        t_d=[(i+x) % 8 for x in range(8)]
                        for x in t_d:
                            if x in poss:
                                nr, nc = r + dym[x], c + dxm[x]
                                new_A[nr][nc][x] += A[r][c][i]
                                break
            else:
                for i in range(8):
                    new_A[r][c][i]+=A[r][c][i]
    A=new_A
def move_to(start,d1,d2,d3):
    dyp, dxp = [-1, 0, 1, 0], [0, -1, 0, 1]
    cy,cx=start
    v_pos=[]
    cnt=0
    for d in [d1,d2,d3]:
        ny, nx = cy + dyp[d], cx + dxp[d]
        if not is_valid(ny,nx): return -1
        if (ny, nx) not in v_pos:
            cnt+=sum(A[ny][nx])
            v_pos.append((ny,nx))
        cy,cx=ny,nx
    return cnt
def search_path(cy,cx):
    best_path=(5,5,5)
    max_mon=-1
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                mon=move_to((cy,cx),d1,d2,d3)
                if mon>max_mon:
                    max_mon=mon
                    best_path=(d1,d2,d3)

    return best_path,max_mon
def move_pacman():
    global pac_pos, m_cnt
    dyp, dxp = [-1, 0, 1, 0], [0, -1, 0, 1]
    py, px = pac_pos
    best_path,max_mon=search_path(py,px)

    for i in range(3):
        ny, nx = py + dyp[best_path[i]], px + dxp[best_path[i]]
        dead = sum(A[ny][nx])
        if dead>0:
            A[ny][nx] = [0] * 8
            A_corpse[ny][nx] = 3
        py,px=ny,nx
    m_cnt-=max_mon
    pac_pos = (py, px)
def delete_corpse():
    global A_corpse
    for r in range(4):
        for c in range(4):
            if A_corpse[r][c]>0:
                A_corpse[r][c] -= 1
def complite_duplication():
    global m_cnt
    for r in range(4):
        for c in range(4):
            for d in range(8):
                A[r][c][d] += A_egg[r][c][d]
                m_cnt += A_egg[r][c][d]
                A_egg[r][c][d] = 0



A = [[[0] * 8 for _ in range(4)] for _ in range(4)]
A_egg = [[[0] * 8 for _ in range(4)] for _ in range(4)]
A_corpse = [[0] * 4 for _ in range(4)]


m, t = map(int, input().split())
pac_pos = tuple(map(lambda x: int(x) - 1, input().split()))

m_cnt=m

for im in range(m):
    r, c, d = map(int, input().split())
    A[r - 1][c - 1][d - 1] += 1

for it in range(t):
    try_duplication()
    move_monster()
    move_pacman()
    delete_corpse()
    complite_duplication()
    if m_cnt==0:
        break

print(m_cnt)
