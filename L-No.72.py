class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        H = len(word1)
        W = len(word2)

        dp = [[0] * (W+1) for _ in range(H+1)]

        # delete
        for r in range(H+1):
            dp[r][0] += r
        for c in range(W+1):
            dp[0][c] += c
        
        for r in range(1, H+1):
            for c in range(1, W+1):
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                
                else: # 3 actions
                    dp[r][c] = 1 + min( dp[r-1][c],   # delete
                                        dp[r][c-1],   # insert
                                        dp[r-1][c-1]) # replace
        return dp[-1][-1]
