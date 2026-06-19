"""I sort the intervals by their end time.

Then I greedily keep the interval that ends earliest.

If the next interval starts before the current end time, it overlaps, so I remove it.

Otherwise, I keep it and update the current end time.

This works because choosing the interval with the earliest end time leaves the most room for future intervals."""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        removed = 0
        pivot = intervals[0][1]

        for s,e in intervals[1:]:
            if s < pivot:
                removed+=1
            else:
                pivot = e
    
        return removed
