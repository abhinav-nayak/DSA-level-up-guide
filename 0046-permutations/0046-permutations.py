class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Since we have to find all possible permutations, it is a hint that backtracking can be used.
        result = []

        def backtrack(perm: List[int], visited: List[bool]):
            # Base condition: if length of permutation is same as input length, then we have found a 
            # valid permutation.
            if len(perm) == len(nums):
                result.append(perm.copy())
                return

            # keep selecting non-visited elements while going downhill in recursion.
            # Once a valid permutation is found, 
            # during uphill pop the last selected element and mark it as not visited.
            for i in range(len(nums)):
                if not visited[i]:
                    perm.append(nums[i])
                    visited[i] = True
                    backtrack(perm, visited)
                    perm.pop()
                    visited[i] = False
        
        backtrack([], [False]*len(nums))
        return result

# Time complexity: O(n! * n)    - n! total permutations will be there and for each permutation
#                                 creating shallow copy will take O(n) time
# Space complexity: O(n! * n) - for output list