"""
I think we cna solve this problem using BFS.

we can scan the grid from the each cell.

When I find a land cell, which is 1, I start BFS from the cell to explore the entire island.

During BFS, I count how many land cells belong to the current island. 
To avoid visiting the same cell again, I mark each visited land cell as 0.

For each cell, I check four direction: up, down, left, right.
If the next cell is inside the grid and is also land, I add it to the queue.

After BFS finisheds, I update the maximum area.
Finally, after checking all cells, I return the maximum island area.
"""
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        H = len(grid)
        W = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def bfs(sr: int, sc: int) -> int:
            queue = deque([(sr, sc)])
            grid[sr][sc] = 0
            area = 0

            while queue:
                r, c = queue.popleft()
                area += 1

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr, nc))

            return area

        max_area = 0

        for r in range(H):
            for c in range(W):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area