"""
We start at index 0, and our goal is to reach the last index.

Each value in nums represents the maximum number of steps we can jump forward from that position.

The key observation is that we do not need to track every reachable index.
Instead, we only need to keep track of the farthest index that can be reached so far.

For each position i, the farthest index we can reach from that position is:

    i + nums[i]

So, during the iteration, we continuously update the farthest reachable index.

If at any point the current index is greater than the farthest reachable index,
it means we cannot reach this position using any previous jump, so the answer is False.

If the farthest reachable index becomes greater than or equal to the last index,
it means we can reach the goal, so the answer is True.

This greedy approach only requires a single pass through the array.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i, jump in enumerate(nums):
            if i > farthest:
                return False

            farthest = max(farthest, i + jump)

            if farthest >= len(nums) - 1:
                return True

        return True
