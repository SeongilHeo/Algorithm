class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        H = len(obstacleGrid)
        W = len(obstacleGrid[0])

        dp = [0] * W
        dp[0] = 1

        for r in range(H):
            for c in range(W):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c > 0:
                    dp[c] += dp[c - 1]

        return dp[-1]
