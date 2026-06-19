"""
We need to find the minimum number of jumps required to reach the last index.

Each value in nums represents the maximum number of steps we can jump forward from that position.

The key idea is to use a greedy approach that is similar to BFS.
We scan the array while keeping track of two values:

    farthest: the farthest index we can reach with one more jump
    cur_end: the end of the current jump range

As we iterate through the current range, we continuously update farthest.
When the current index reaches cur_end, it means we have finished checking all positions
that are reachable with the current number of jumps.

At that point, we need to make one more jump, so we increase the jump count
and update cur_end to farthest.

We stop before the last index because once we reach the last index,
we do not need to jump again.
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_end = 0
        farthest = 0
        steps = 0

        for idx in range(len(nums)-1):
            farthest = max(farthest, idx+nums[idx])

            if idx == cur_end:
                steps += 1
                cur_end = farthest

        return steps