class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map for O(1) lookup
        hashMap = dict()

        for i, n in enumerate(nums):
            num2 = hashMap.get(target-n)
            if num2 is not None:
                return i, num2
            hashMap[n] = i

        