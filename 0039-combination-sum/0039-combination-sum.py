class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Since we have to find 'all unique combinations', it is a hint that backtracking can be used.
        result = []

        combination = []
        def dfs(i: int, summ: int):
            # if summ >= target, we have hit dead-end
            if summ >= target or i>=len(candidates):
                if summ == target:
                    # shallow copy is needed to prevent data corruption
                    result.append(combination.copy())
                return

            # consider candidates[i] for solution
            combination.append(candidates[i])
            dfs(i, summ +candidates[i])
            # backtrack: undo previous step of adding candidates[i] in combination
            combination.pop()
            # explore other paths
            dfs(i+1, summ)

        
        dfs(0, 0)
        return result

# Time complexity: O(2^(t/m))
#                  Time complexity of binary tree is 2^height. Even if all elements are equal to minimum value, height=t/m
# Space complexity: O(t/m)  for recursion stack (=height of tree)
# where t is the given target and m is the minimum value in candidates list.
