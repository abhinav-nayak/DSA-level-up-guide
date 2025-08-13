class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map for O(1) lookup
        hashMap = dict()

        # iterate and find if suitable pair exists, else update hash map
        for i, n in enumerate(nums):
            num2 = hashMap.get(target-n)
            # NOTE: if num2 is 0, then just 'if num2:' condition won't work
            if num2 is not None:
                return i, num2
            hashMap[n] = i

# Time complexity: O(n)      
# Space complexity: O(n)