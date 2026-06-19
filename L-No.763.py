"""
We need to partition the string so that each character appears in at most one partition.

The key idea is to know the last position of each character.
If a character appears in the current partition, the partition must include that character's last occurrence.

First, I use a dictionary to store the last index of each character.

Then, I iterate through the string and maintain an end index for the current partition.
For each character, I update end to the farthest last occurrence among the characters seen so far.

When the current index becomes equal to end, it means all characters in the current partition
finish within this range, so we can safely cut the string here.

To calculate the length of each partition, I also keep a start index.
When we cut a partition, its length is:

    end - start + 1

Then I append that length to the result list and move start to the next index.
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {}

        for idx, ch in enumerate(s):
            last_pos[ch] = idx

        result = []
        start = 0
        end = 0

        for idx, ch in enumerate(s):
            end = max(end, last_pos[ch])

            if idx == end:
                result.append(end - start + 1)
                start = idx + 1

        return result
