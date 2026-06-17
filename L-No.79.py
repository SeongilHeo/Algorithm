# Yes, I think we can solve this problem using DFS with backtracking.

# We need to check whether the given word exists as a path in the grid.
# Since the path can start from any cell, we can run DFS from each cell as a starting point.

# The DFS function will be recursive.
# At each recursive call, we check whether the current cell matches the current character in the word.
# If it matches, we move to the next character and continue searching in four directions.

# This is also a backtracking approach because we temporarily mark a cell as visited,
# explore possible paths from that cell, and then restore the cell before returning.

# For the base case, if the current index reaches the last character of the word
# and the character matches, then we have found a valid path.

# We also need to check the boundary and avoid revisiting the same cell,
# because the problem states that the same letter cell cannot be used more than once.

# To mark a cell as visited, I will temporarily replace it with a special character, '#'.
# Then, I will recursively call DFS in four directions: up, down, left, and right.
# If any of those recursive calls returns True, it means we found a valid path.

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