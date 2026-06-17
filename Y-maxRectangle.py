# We need to find the largest rectangle that contains only 1s.

# The main idea is to treat each row as the bottom of a rectangle.
# For each row, I'll treat the 1s as building heights. I'll keep track of how tall the "column" of 1s up to that row.
# This gives us a histogram for each row.
# And then I'll use a stack-based approach to find the largest rectangle area in this historgram.

# For example, the height list can be updated row by row like this:

# 0 1 1 1 1 -> heights = [0, 1, 1, 1, 1]
# 1 1 1 1 0 -> heights = [1, 2, 2, 2, 0]
# 0 1 1 1 0 -> heights = [0, 3, 3, 3, 0]
# 1 1 1 1 0 -> heights = [1, 4, 4, 4, 0]
# 1 1 1 1 0 -> heights = [2, 5, 5, 5, 0]
# 0 0 0 0 0 -> heights = [0, 0, 0, 0, 0]

# After building the height list for each row, we calculate the largest rectangle area
# in that histogram.

# To solve the histogram problem efficiently, we use a monotonic increasing stack.
# The stack stores indices of the heights.
# When we meet a smaller height, it means the previous taller bar cannot extend further
# to the right, so we pop it and calculate the rectangle area using that height.

# The outer loop updates the histogram heights for each row.
# The helper function finds the maximum rectangle area for the current histogram.

def maximalRec(A):
    row = len(A)
    col = len(A[0])

    heights = [0] * col # heights[c] stores the number of consecutive 1s ending at the current row in column c.
    max_area = 0 
    for r in range(row):
        for c in range(col):
            if A[r][c] == 1: # If the cell is 1, extend the height for this column.
                heights[c]+=1
            else:   # If the cell is 0, the consecutive sequence is broken.
                heights[c] = 0
        max_area = max(max_area, largestRecArea(heights)) # Compute the largest rectangle area for the current histogram.

    return max_area
    

def largestRecArea(heights):
    stack = [] # The stack stores indices of heights in increasing order.
    max_area = 0
    heights.append(0) # Add a sentinel value to flush out the remaining heights in the stack.
    for idx, h in enumerate(heights): # Iterate over each height in the histogram.
        while stack and heights[stack[-1]] > h: # If the current height is smaller, calculate areas for taller previous bars.
            height = heights[stack.pop()]

            if stack:
                width = idx - stack[-1] - 1
            else:
                width = idx

            max_area = max(max_area, height*width)

        stack.append(idx)

    heights.pop()

    return max_area

A = [[0, 1, 1, 1, 1],
[1, 1, 1, 1, 0],
[0, 1, 1, 1, 0],
[1, 1, 1, 1, 0],
[1, 1, 1, 1, 0],
[0, 0, 0, 0, 0]]

print(maximalRec(A))