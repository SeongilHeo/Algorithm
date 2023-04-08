global locations, dx, dy, weapon, board, n, m, k, directions, firstPower

# 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def getGunInfo():
    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(n):
            if a[j]==0:
                continue
            else:
                board[i][j].append(a[j])

def getUserInfo():
    for _ in range(m):
        aa = list(map(int, input().split()))
        x, y, d, s = aa[0], aa[1], aa[2], aa[3]
        locations.append([x - 1, y - 1])
        directions.append(d)
        firstPower.append(s)

def move(i):
    x, y, = locations[i]
    d = directions[i]

    nx = x + dx[d]
    ny = y + dy[d]

    # 격자 범위 벗어나면
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        # 정반대로 방향 변경
        nd = (d + 2)%4

        nx = x + dx[nd]
        ny = y + dy[nd]
        # 플레이어 위치,방향 업데이트
        directions[i] = nd

    locations[i] = nx, ny

# 현재 유저, 해당 유저의 x좌표, y좌표
def isUserExisted(i, user_x, user_y):
    for j in range(m):
        # 자기 자신 아니고
        if j != i:
            # x,y 좌표 똑같다면, 해당 위치에 다른 플레이어 존재
            if user_x == locations[j][0] and user_y == locations[j][1]:
                return j
    return

# 유저번호, 총이 있는 좌표
def getGun(i):
    x,y=locations[i]
    if not board[x][y]:
        return 
    # 놓여져 있는 총과 유저가 가진 총 중에서 더 센 총 획득
    userGun = weapon[i]
    putGunsMax = max(board[x][y])

    # 놓여져 있는 총이 더 쎄다면
    if putGunsMax > userGun:
        # user가 총이 있으면
        if userGun !=0:
            # 바닥에 내려놓기
            board[x][y].append(userGun)

        # 가장 쎈 총 획득
        board[x][y].remove(putGunsMax)
        weapon[i]=putGunsMax
    # 유저가 가진 총이 더 쎄다면 아무 것도 하지 않음

# 이동한 다음
def after_move(i):
    x, y = locations[i]
    otherUser = isUserExisted(i, x, y)
    
    # 플레이어 없다면
    if otherUser is None:
        getGun(i)
    # 플레이어가 있다면 싸우기
    else:
        fight(i,otherUser)

def fight(user1, user2):
    user1_info = firstPower[user1] + weapon[user1]#power1
    user2_info = firstPower[user2] + weapon[user2]#power2

    if user1_info > user2_info:
        winner = user1
        loser = user2
    elif user1_info == user2_info:
        if firstPower[user1] > firstPower[user2]:
            winner = user1
            loser = user2
        else:
            winner = user2
            loser = user1
    else:
        winner = user2
        loser = user1

    # loser action
    loser_action(loser)
    
    # winner action
    # 각 플레이어의 초기 능력치와 갖고있는 총의 공격력의 합의 차이만큼 포인트 획득
    points[winner] += abs(user1_info - user2_info)
    getGun(winner)
        
# 싸움에서 진 플레이어
def loser_action(loser):
    # 본인이 가진 총을 해당 격자에 모두 내려놓기
    if weapon[loser]!=0:
        board[x][y].append(weapon[loser])
        weapon[loser]=0

    # 이동
    x, y = locations[loser]
    d = directions[loser]
    nx = x + dx[d] # 이동할 곳
    ny = y + dy[d]

    # 다른 플레이어 존재하거나 격자 벗어나면
    while isUserExisted(loser, nx, ny) or nx < 0 or nx >= n or ny < 0 or ny >= n:
        # 오른쪽으로 90도씩 회전
        d=(d+1)%4
        nx=x+dx[d]
        ny=y+dy[d]

    # 이동 & 방향 업데이트
    locations[loser] = nx, ny
    directions[loser]=d
    
    # 해당 칸에 총이 있다면
    getGun(loser)

n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
locations = []
directions = []
weapon = [0]*m
firstPower = []
points = [0] * m

getGunInfo()
getUserInfo()

for i in range(k):
    for user in range(m):
        move(user)
        after_move(user)

for i in points:
    print(i, end=" ")