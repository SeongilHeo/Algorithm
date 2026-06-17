# https://www.youtube.com/watch?v=Ti5vfu9arXQ

A = [[0, 1, 1, 1, 1],
     [1, 1, 1, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]

H = len(A)
W = len(A[0])


dp = [[0]*W for _ in range(H)]

for y in range(H):
    for x in range(W):
        if A[y][x] == 1:
            continue
        if y==0 or x==0:  # boundary condition
            dp[y][x] = 1
            continue
        dp[y][x] = min(dp[y-1][x-1], 
                      dp[y-1][x  ], 
                      dp[y  ][x-1]) + 1
max(sum(dp,[]))

# May I take a moment to read the problem and think about it?

# Yes I have a question.
# Is The grid always a square, or can it be a rectangle?
# Thank you for clarification.

# First of all, I can start with a naive approach.
# I can consider each cell as a starting point and try to expand a square from that position.
# For example, 
# if i start from [0,0], I can check whether a 2x2, 3x3, 4x4, annd so on. to the min of width and height of grid
# 0,0
# [0,0], [0,1], [1,0], [1,1]
# [0,0], [0,1], [0,2], [1,0], [1,1] [1,2],[0,2],[1,2],[2,2]
# Once I find a 0, I know the square is not valid, so I can stop expanding.

# But, this is definitely inefficeint becuase we need to check the sma cells repeatedly for different staring points.

# So, to optimize it, we can use dynamic programming approach.

# For the dp approach, I want to avoid repeated computation by reusing previously computed result. 
# I will define dp[y][x].
# dp[y][x] means the largest square size ending at (y, x).
# So I consider each cell as the bottom-right coner of square.

# The first row and first colum are boundary case, so if the cell is 1, then dp[y][x] is 1; otherwize, it is 0.

# For the other cells, if the current is 1, I only need to check three neighboring position: the top, left, and the top-left diagonal.
# The recurrence relation is. dp[y,x] = min(dp[y-1,x-1],dp[y-1,x],dp[y,x-1]) + 1

# We take the minimum because a square can only be expanded if all three neighboring directions can support it. 

# For exmaple, if the grid is 
# 1 1 1
# 1 1 1
# 1 1 1
# this dp table becomes
# 1 1 1
# 1 2 2
# 1 2 3

# The largest side length is 3, so the maximum square area is 3*3 = 9 
