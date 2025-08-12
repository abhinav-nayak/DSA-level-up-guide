class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create hash set for O(1) look up
        hashSet = set()
        for n in nums:
            if(n in hashSet):   # O(1) operation
                return True
            hashSet.add(n)
        return False

# Time complexity: O(n)      
# Space complexity: O(n)