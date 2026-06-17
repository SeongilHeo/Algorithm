# We need to generate all possible letter combinations.
# First, we create a mapping for the digit-to-letters.
# and then, we will use a backtracking approach.

# To do this, we use two dynamic array, result and path. 
# result is that we return, and the path is a partial solution.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dmap = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz'
        }
        
        result = []
        path = []
        # this backtrack function will be recursive by adding the next char at the each recurssive step.
        def backtrack(idx):
            # Our the base case is the index reaches the length of digigs. which means we get one complete combination.
            if idx == len(digits):
                result.append("".join(path))
                return
            
            # using the digit to letter dictionary, we can get the corresponding letters
            current_digit = digits[idx]
            letters = dmap[current_digit]

            # and for each char in letteres, we will append that letter into the path
            for ch in letters:
                path.append(ch)
                # after that we call backtrack function with next index
                # (which means we move to the next digit)
                backtrack(idx+1)
                # after getting the return from the recusive backtrack fuction, we will remove the last element from the path o explore other possibilities.
                path.pop()

        # Outside of the function, we can start calling the backtrack fucntion with index 0, from the first digit.
        backtrack(0)

        # through the backtracking method we can get the all possilbe letter combination of given digits.
        # so we return that result
        return result
        