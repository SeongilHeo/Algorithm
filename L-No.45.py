"""
we need to find the minimum number of jumps

and nums array represents the maximum jump steps.
this means all previous cells are reachable after jump forward.

for example if we jump from index 0 to index 3, indcies 0,1,2,3 are reachable within same number of jump

So we can only consider farthest index, and we can increase jumps count after the farthest index

but the farthest value will keep change by iterating the index,
so I will use an additional value called cur_end,
when current index becomes equal to cur_end, we can increase the jump number and the cur_end update to farthest
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
            