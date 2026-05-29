# 5
# N, M : row, col
# >, v, <, ^
# Case 1
board=[[0, 2, 2, 0, 0, 0, 0, 0],
       [0, 2, 2, 0, 0, 4, 4, 0],
       [0, 3, 3, 3, 1, 4, 4, 0],
       [0, 3, 3, 3, 0, 0, 0, 0],
       [0, 3, 3, 3, 5, 5, 6, 0], 
       [0, 0, 0, 0, 5, 5, 0, 0]]
commands=[[3,1],[3,1]]
result=[[0, 0, 2, 2, 0, 0, 0, 0],
        [4, 4, 2, 2, 0, 0, 0, 0], 
        [4, 4, 0, 3, 3, 3, 1, 0], 
        [0, 0, 0, 3, 3, 3, 0, 0],
        [6, 0, 0, 3, 3, 3, 5, 5], 
        [0, 0, 0, 0, 0, 0, 5, 5]]
# # Case 2
board=[
    [0,9,1,1,6,0,0,0],
    [2,2,1,1,0,0,0,0],
    [2,2,3,4,4,4,0,0],
    [5,0,0,4,4,4,7,0],
    [0,0,0,4,4,4,8,8],
    [0,0,0,0,0,0,8,8]]
commands=[[2,1],
          [3,1],
          [9,2],
          [4,1]]
result=[[8, 8, 0, 1, 1, 6, 0, 0],
        [8, 8, 0, 1, 1, 0, 0, 0],
        [4, 4, 4, 9, 3, 0, 0, 0],
        [4, 4, 4, 7, 2, 2, 0, 0],
        [4, 4, 4, 0, 2, 2, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0]]
# # Case 3
board=[[1,1,0],
       [1,1,0]]
commands=[[1,4],
          [1,3],
          [1,2]]
result=[[0, 1, 1],
        [0, 1, 1]]

# ------------------------------
def get_box_info(board):
    # return start point and size
    N = len(board)
    M = len(board[0])
    box = {}
    for row in range(N):
        for col in range(M):
            print
            if board[row][col] !=0:
                id = board[row][col]
                if box.get(id):
                    box[id][-1] += 1
                else:
                    box[id] = [row,col,1]
    for b in box.values():
        b[-1]=int(b[-1] ** (1/2))
    return box

dy=[0,0,1,0,-1]
dx=[0,1,0,-1,0]

from collections import deque

def solution(board, commands):
    N,M = len(board),len(board[0])
    Box=get_box_info(board)
    # Each command
    for box_id, head in commands:
        que = deque([(box_id, head)])
        while que:
            box_id,head=que.popleft()
            # current
            start_y, start_x, size = Box[box_id]
            # clean current position
            for py in range(start_y,start_y+size):
                for px in range(start_x,start_x+size):
                    py,px=py%N,px%M
                    if board[py][px]==box_id:
                        board[py][px]=0
            # get next start point
            new_y=(start_y+dy[head]) % N
            new_x=(start_x+dx[head]) % M
            # set next start point
            Box[box_id]=[new_y,new_x,size]
            
            # put into que for overlap box and outrange itself
            overlap=set()   
            outrange=False
            for ny in range(new_y,new_y+size):
                for nx in range(new_x,new_x+size):
                    if 0<=nx<M and 0<=ny<N: # inrange
                        if board[ny][nx] !=0 : # overlapped
                            overlap.add(board[ny][nx])
                        board[ny][nx] = box_id # mark
                    else:                   # outrange
                        ny,nx=ny%N,nx%M     # get new inragne position
                        if board[ny][nx] !=0 : # overlapped
                            overlap.add(board[ny][nx])
                        board[ny][nx] = box_id #mark
                        outrange=True # mark for quing
            
                        
            for o in overlap:
                que.append((o,head))
            if outrange:
                que.append((box_id, head))
    return board

solution(board, commands)