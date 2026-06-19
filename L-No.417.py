"""
Instead of checking whether water from each cell can reach both oceans,
I start from each ocean and move in the reverse direction.

In the original direction, water can flow from a higher or equal cell to a lower or equal cell.

So in the reverse direction, I can move from the ocean side to a neighboring cell only if the neighbor's height is greater than or equal to the current cell's height.

I run BFS once from all Pacific border cells and once from all Atlantic border cells.

Then, any cell that is reachable from both searches can flow to both oceans.
"""
from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        H = len(heights)
        W = len(heights[0])

        def bfs(starts):
            visited = set()
            queue = deque(starts)

            for r,c in starts:
                visited.add((r,c))
            
            while queue:
                r,c, = queue.popleft()

                for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr = r + dr
                    nc = c + dc
                    
                    if (
                        0 <= nr < H and
                        0 <= nc < W and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visited((nr,nc))
                        queue.append((nr,nc))
            return visited
        
        pacific_starts = []
        atlantic_starts = []

        # O(M)
        for r in range(H):
            pacific_starts.append((r,0))
            atlantic_starts.append((r, W-1))
        
        # O(N)
        for c in range(W):
            pacific_starts.append((0,c))
            atlantic_starts.append((H-1, c))
        
        # 2* O(M*N)
        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        result = []

        # 2* O(M*N)
        for r in range(H):
            for c in range(W):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])

        return result
            
