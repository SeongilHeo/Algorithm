"""I use Kadane’s algorithm.

At each position, I keep track of the maximum subarray sum ending at the current number.

For each number, I have two choices:
    1. Start a new subarray from the current number
    2. Extend the previous subarray by adding the current number

Then I update the global maximum sum.

At the end, the global maximum is the answer.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumsum = nums[0]
        maxsum = nums[0]

        for n in nums[1:]:
            cumsum = max(n, cumsum+n)
            maxsum = max(maxsum,cumsum)
        return maxsum