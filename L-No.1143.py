
class Solution:
    def longestCommonSubsequence2D(self, text1: str, text2: str) -> int:
        H = len(text1)
        W = len(text2)
        dp = [[0]* (W+1) for _ in range(H+1)]

        for r in range(1,H+1):
            for c in range(1,W+1):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = dp[r-1][c-1]+1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]

    def longestCommonSubsequence1D(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for ch1 in text1:
            prev = 0

            for c in range(1, len(text2) + 1):
                temp = dp[c]

                if ch1 == text2[c - 1]:
                    dp[c] = prev + 1
                else:
                    dp[c] = max(dp[c], dp[c - 1])

                prev = temp

        return dp[-1]