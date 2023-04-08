import math
global locations, dx, dy, weapon, board, n, m, k, directions, firstPower

# 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def getGunInfo():
    for i in range(n):
        a = list(map(int, input().split()))
        for j in a:
            board[i].append([j])


def getUserInfo():
    for i in range(m):
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
        newd = d + 2
        if newd > 3:
            newd -= 4

        nnx = x + dx[newd]
        nny = y + dy[newd]
        # 플레이어 위치,방향 업데이트
        locations[i] = nnx, nny
        directions[i] = newd
    else:
        locations[i] = nx, ny


# 현재 유저, 해당 유저의 x좌표, y좌표
def isUserExisted(i, user_x, user_y):
    for j in range(m):
        # 자기 자신 아니고
        if j != i:
            # x,y 좌표 똑같다면, 해당 위치에 다른 플레이어 존재
            if user_x == locations[j][0] and user_y == locations[j][1]:
                return j
    return "no"

# 격자에 총이 존재하는지?
def isGunExisted(x, y):
    for i in range(len(board[x][y])):
        if board[x][y][i] == 0:
            return False
    return True


# 유저번호, 총이 있는 좌표
def getGun(i, gun_x, gun_y):
    # 놓여져 있는 총과 유저가 가진 총 중에서 더 센 총 획득
    putGunsMax, userGunsMax = 0, 0
    putGunsMax = max(board[gun_x][gun_y])

    # 유저가 갖고있는 총 중에 가장 쎈 총
    for j in range(len(weapon[i])):
        if userGunsMax < weapon[i][j]:
            userGunsMax = weapon[i][j]

    # 놓여져 있는 총이 더 쎄다면
    if putGunsMax > userGunsMax:
        for g in weapon[i]:
            # 바닥에 내려놓기
            board[gun_x][gun_y].append(g)
        weapon[i] = []

        # 가장 쎈 총 획득
        weapon[i].append(putGunsMax)
        board[gun_x][gun_y].remove(putGunsMax)

        if not board[gun_x][gun_y]:
            board[gun_x][gun_y] = [0]

    # 유저가 가진 총이 더 쎄다면 아무 것도 하지 않음

# 이동한 다음
def after_move(i):
    x, y = locations[i]
    otherUser = isUserExisted(i, x, y)

    # 플레이어 없다면
    if otherUser == "no":
        # 해당 칸에 총 있음
        if isGunExisted(x, y):

            # 총을 갖고 있지 않다면
            if len(weapon[i]) == 0:
                # 총 획득
                for j in board[x][y]:
                    weapon[i].append(j)

                # 맵에서 총 지우기
                board[x][y] = [0]

            # 플레이어가 이미 총 가짐
            else:
                getGun(i, x, y)

        # 해당 칸에 총 없으면 패스

    # 플레이어가 있다면 싸우기
    else:
        fight(i, otherUser)

# 유저의 총의 공격력 합 구하기
def calSumGunPower(user):
    power = 0
    for i in range(len(weapon[user])):
        power += weapon[user][i]

    return power


def fight(user1, user2):
    power1, power2 = calSumGunPower(user1), calSumGunPower(user2)
    user1_info = firstPower[user1] + power1
    user2_info = firstPower[user2] + power2

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

    # 각 플레이어의 초기 능력치와 갖고있는 총의 공격력의 합의 차이만큼 포인트 획득
    points[winner] += abs(user1_info - user2_info)
    loser_action(loser, locations[loser][0], locations[loser][1])
    getGun(winner, locations[winner][0], locations[winner][1])


# 싸움에서 진 플레이어
def loser_action(loser, x, y):
    # 본인이 가진 총을 해당 격자에 모두 내려놓기
    for i in weapon[loser]:
        board[x][y].append(i)
        weapon[loser] = []

    # 이동
    userx, usery = locations[loser]
    d = directions[loser]
    nx = userx + dx[d]
    ny = usery + dy[d]

    # 다른 플레이어 존재하거나 격자 벗어나면
    if isUserExisted(loser, nx, ny) != "no" or nx < 0 or nx >= n or ny < 0 or ny >= n:
        # 오른쪽으로 90도 회전
        for i in range(1, 4):
            newd = d + i
            if newd > 3:
                newd -= 4
            nnx = userx + dx[newd]
            nny = usery + dy[newd]

            if isUserExisted(loser, nnx, nny) == "no":
                locations[loser] = nnx, nny
                directions[loser] = newd
                break

    else:
        locations[loser] = nx, ny

    # 해당 칸에 총이 있다면
    movedUserX, movedUserY = locations[loser]
    if isGunExisted(movedUserX, movedUserY):
        getGun(loser, movedUserX, movedUserY)


n, m, k = map(int, input().split())
board = [[] for _ in range(n)]
locations = []
directions = []
weapon = [[] for _ in range(m)]
firstPower = []
points = [0] * m

getGunInfo()
getUserInfo()
cur = 0

while cur < k:
    for user in range(m):
        move(user)
        after_move(user)
    cur += 1

for i in points:
    print(i, end=" ")