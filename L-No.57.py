"""Since the intervals are already sorted and non-overlapping, I do not need to sort them again.

I divide the process into three parts.

First, I add all intervals that come completely before the new interval.

Second, while intervals overlap with the new interval, I merge them by updating the start and end of newInterval.

Finally, I add the remaining intervals that come completely after the merged interval.

Then I return the result."""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        results = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            results.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i+=1
        results.append(newInterval)

        while i<n:
            results.append(intervals[i])
            i+=1

        return results
