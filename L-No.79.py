class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        H = len(board)
        W = len(board[0])

        def dfs(r: int, c: int, idx: int) -> bool:
            # If the current cell does not match the current character,
            # this path is invalid.
            if r < 0 or r >= H or c < 0 or c >= W or board[r][c] != word[idx]:
                return False

            # If this is the last character and it matches,
            # we found the word.
            if idx == len(word) - 1:
                return True

            # Mark the current cell as visited temporarily.
            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )

            # Restore the original character for other paths.
            board[r][c] = temp

            return found

        for r in range(H):
            for c in range(W):
                if dfs(r, c, 0):
                    return True

        return False