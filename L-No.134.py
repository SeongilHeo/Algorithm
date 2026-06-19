"""
We need to find a starting gas station index that allows us to complete one full circular route.

At each station, the net gas we gain is:

    gas[i] - cost[i]

If the total gas is less than the total cost, then completing the circuit is impossible,
so we return -1.

Otherwise, we can use a greedy approach to find the starting index.

We keep track of the current tank while scanning the stations.
If tank becomes negative at index i, it means the current starting point cannot reach station i + 1.

Also, any station between the current start and i cannot be a valid starting point either,
because starting from the middle would have even less accumulated gas.

So, we set the next station, i + 1, as the new starting candidate and reset tank to 0.

At the end, if the total net gas is non-negative, the start index is the answer.
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for idx in range(len(gas)):
            diff = gas[idx] - cost[idx]

            total += diff
            tank += diff

            if tank < 0:
                start = idx + 1
                tank = 0
        if total < 0:
            return -1

        return start