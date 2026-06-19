from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        last = 0

        H = len(grid)
        W = len(grid[0])

        rotten = deque()
        fresh = 0

        for r in range(H):
            for c in range(W):
                if grid[r][c] == 2:
                    rotten.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while rotten:
            cy,cx,time = rotten.popleft()

            last = max(time, last)

            for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
                ny=cy+dy
                nx=cx+dx

                if 0 <= ny < H and 0 <= nx <W and grid[ny][nx]==1:
                    grid[ny][nx] = 2
                    rotten.append((ny,nx,time+1))
                    fresh -= 1
                    
        if fresh > 0:
            return -1
        return last