class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Since we have to find 'all possible subsets', it is a hint that backtracking can be used.
        result = []

        subset = []
        def dfs(i: int):
            if i>=len(nums):
                # shallow copy is needed to avoid data corruption
                result.append(subset.copy())
                return

            # i represents the position of input for which we are making a decision
            subset.append(nums[i])
            dfs(i+1)
            # backtrack: undo previous decision of including nums[i] in subset
            subset.pop()
            # explore another path by not including nums[i] in subset
            dfs(i+1)

        dfs(0)
        return result

# Time complexity: O(n*(2^n))
#                  In decision tree, the number of leaf nodes (i.e. no. of solutions) = 2^n
#                  Each solution can have max of n nodes.
#                  So, O(n*(2^n))
# Space complexity: O(n) - extra space for recursion stack
#                   O(2^n) - space for output list
