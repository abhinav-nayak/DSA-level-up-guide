class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # To avoid duplicate combinations like [1, 7] and [7, 1]:
        # 1. Sort the input
        # 2. While backtracking, if candidates[i] is popped then don't consider other values equal to candidates[i] as all combinations
        # with candidates[i] value is explored.
        candidates.sort()

        # Since we are asked to 'find all unique combinations', it is a hint that backtracking can be used.
        result = []

        subset = []
        def dfs(i: int, summ: int):
            # base condition
            if i>=len(candidates) or summ>=target:
                if summ==target:
                    # shallow copy to prevent corruption of result list
                    result.append(subset.copy())
                return

            # keep making choices/ chossing path and update hash map
            subset.append(candidates[i])
            dfs(i+1, summ+candidates[i])
            # backtrack: undo previous step of choosing candidates[i]
            subset.pop()
            # explore further paths by not considering candidates[i]
            # to avoid duplicates as explained above
            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, summ)

        dfs(0, 0)
        return result
