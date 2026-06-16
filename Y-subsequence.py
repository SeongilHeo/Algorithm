# from bisect import bisect_right
# from collections import defaultdict

def numMatchingSubseq(s, words):
    position = {chr(i):[] for i in range(97, 97+26)}
    # position = defaultdict(list)

    for i, ch in enumerate(s):
        position[ch].append(i)
    cnt = 0

    for word in words:
        curr = -1
        matched = True

        for c in word:
            pos_list = position[c]

            idx = bisect_right(pos_list, curr)
            if idx == len(pos_list):
                matched = False
                break
            
            curr = pos_list[idx]

        if matched:
            cnt += 1
    return cnt

def bisect_right(pos, cur):
    l, r = 0, len(pos)

    while l< r:
        mid = l+(r-l)//2
        if pos[mid] <= cur:
            l = mid + 1
        else: # pos[mid] >  cur:
            r = mid
    return l


def bisect_left(pos, cur):
    l, r = 0, len(pos)

    while l < r:
        # mid = l+(r-l)//2 /
        if pos[mid] < cur:
            l = mid + 1
        else: # pos[mid] >  cur:
            r = mid
    return l

def bisect(pos, cur):
    l, r = 0, len(pos)

    while l < r:
        mid = l+(r-l)//2
        if pos[mid] == cur:
            return mid
        elif pos[mid] < cur:
            l = mid + 1
        else: # pos[mid] >  cur:
            r = mid
    return -1

s = 'abcbde'
words = ['a', 'bbc', 'acd', 'ace']
print(numMatchingSubseq(s, words))


# I want to restate the problem first. 
# Subsequence means that the characters should appear in the same order, but they do not need to be contiguous.

# For instance, if the string s is "abcde" and the words array is ["ace", "bb"]. "ace" is valid subsequence because its characters appear in same order as in s, but "bb" is not valid because string s only contains one "b".

# The first solution that comes to mind is a burte-force approach. 

# For each word, I can use two pointers. I scan through s and try to match its chacters one by one. If I can match all characters, then the word is a subsequence.

# But, this approach should scan the same string s again for every word.

# To optimize this, I will preprocess s by storing the position of each character in a dictionary. 

# At this point, I have question: can string s contain duplicate character?
# If so, I should store all indices for each character, not just one index. 
# So I will use a defaultdict with an empty list, [].

# Then, for each word, I keep track of the previous matched index.
# For each chacter in the word, I need to find the first occurrence that appear after the previous index. 
# Since the posiion list is sorted, I can use binary search.

# ---
# So let me start to implement this.

# First of all, 

# I will create a dictionary called positions. The key is character, and the value is a list of indices where that character appears in s.

# Then i will iterate over each word in words.

# For each word, I initialize prev to -1, because before matching any character, there is no previous index. 

# For each character in the word, I get its position list from the dictinoary.  I will call this pos_list.

# "Here, pos_list store all indices where the current charactr appear in s."
# Then I use binary search to find the first index in pos_list that is greater than prev.

# "if idx reaches the end of the list, it means there is no valid position for this character after preve."
# If the result is equal to the length of pos_list, it means there is no valid next position, so this word is not a subsequence.

# Otherwise, I update prev to that matched position and continue chekcing the next character.

# If all chacters are matched successfully, I increase the answer by one.

# ---
# bisect_right performs binary search on a sorted list.
# it find the first index where the value is greater than the target.

# bisect_right performs binary search on a sorted list.
# it find the first index where the value is greater than or equal to the target.





