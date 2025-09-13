class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Since we have to find 'all possible' subsets, we can think of backtracking
        result = []

        # To avoid duplicate combinations like [1, 7] and [7, 1]:
        # 1. Sort the input
        # 2. While backtracking, if candidates[i] is popped then don't consider other values equal to 
        # candidates[i] as all combinations with candidates[i] value is explored.
        nums.sort()

        subset = []
        def dfs(i: int):
            if i >= len(nums):
                # shallow copy is needed for result data corruption
                result.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)

            # backtrack: de-select nums[i]
            # While backtracking, if candidates[i] is popped then don't consider other values equal to 
            # candidates[i] as all combinations with candidates[i] value is explored.
            subset.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)

        dfs(0)
        return result

# Time complexity: O(n * 2^n) - 2^n possible solutions and for each solution shallow copy takes O(n) time.
# Space complexity: O(n) - recursion stack