# Yes. Umm...
# I think we can use DFS algorithm.

# we need to find the path including the word at the grid map.
# so we can run the DFS algorithm from each cell as start point.
# the DFS fucntion will be recursive, and each recursion stage we can get the next character.
# We can say it is a backtracking approache for DFS.

# Let's implement it.
# dfs function is the recursive fuction so we need a base case. 
# when the index reach the length of the word we can say we hit the solution.

# and we also need to check is in boundary and visited becuase they said "the same letter cell may not be used more than once."

# I will swich the cell to special character '#' temporary to mark as the cell is visited.
# and the call the dfs fucntion recursive toward 4 dirction.
# if one of them get the True result, we got the possible path.

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