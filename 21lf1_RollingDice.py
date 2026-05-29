n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
score = 0
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [[False] * n for _ in range(n)]

dice = [1, 2, 3, 6, 5, 4]
dice_pos = (0, 0)
dice_base = 1
dice_head = 1

def is_valid(y, x):
    return 0 <= y < n and 0 <= x < n

def search_sames(cy, cx, num):
    global cnt
    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]
        if is_valid(ny, nx) and A[ny][nx] == num and not visited[ny][nx]:
            cnt += 1
            visited[ny][nx] = True
            search_sames(ny, nx, num)

def sum_sames(cy, cx):
    global score, cnt, visited
    cnt = 1
    num = A[cy][cx]
    visited = [[False] * n for _ in range(n)]
    visited[cy][cx] = True

    search_sames(cy, cx, num)
    score += num * cnt

def roll_dice():
    global dice_pos, dice_head, dice

    cy, cx = dice_pos  # pos dice base head
    ny, nx = cy + dy[dice_head], cx + dx[dice_head]
    if not is_valid(ny, nx):
        dice_head = (dice_head + 2) % 4
        ny, nx = cy + dy[dice_head], cx + dx[dice_head]
    dice_pos = (ny, nx)

    a1, b2, c3, d6, e5, f4 = dice
    if dice_head == 0:
        dice = [b2, d6, c3, e5, a1, f4]  # ^
    elif dice_head == 1:
        dice = [f4, b2, a1, c3, e5, d6]  # >
    elif dice_head == 2:
        dice = [e5, a1, c3, b2, d6, f4]  # v
    elif dice_head == 3:
        dice = [c3, b2, d6, f4, e5, a1]  # <

    dice_base = dice[3]

    sum_sames(ny, nx)

    if A[ny][nx] > dice_base:
        dice_head = (dice_head - 1) % 4
    elif A[ny][nx] < dice_base:
        dice_head = (dice_head + 1) % 4


for _ in range(m):
    roll_dice()

print(score)