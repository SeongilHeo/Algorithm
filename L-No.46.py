# To get all permuations of given numbers
# I can use backtracking approach.
# The idea is to build each permutation step by step.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return res


# To do this, we need a result list for all completed permutations, a path list for the current permutation, and a used list to track which numbers have already been included.

# The backtrack function tries to add an unused number to the path, recursively.

# At each recursive step, I iterate through nums and choose one unused number.

# I add that number to the path, mark it as used, and then recursively move on to the next position.

# Since the backtracking function is recursive, we need a base case.
# The base case is when the length of the path becomes equal to the length of nums.

# At this point, we have completed one permutation, so I add a copy of the path to the result.

# After the recursive call returns, I remove the last number from the path and mark it as unused again, so that I can try other choices.


# We will actually write this ourselves. 

# So we will get n is the length of the numbers, and we will get two dynamic array, answer and sol.
# answer is that we return, and sol is a partial solution.

# Now, our backtrack fucntion will be recursive. 

# Our base case is our length of solution is n, we hit a solution. 

# So we will answer append a solution copy. And from there, we just return.

# Now, here's the trick. For each x in the numbers, if thatnumbers is not is our solution, then we will append that nubmer, recursively.

# Call our backtrack function, and when we return we need to pop that same number off.

# Outside we can simply just call our backtrack function once. 
# That'll poplutate answer, and we can return that. 