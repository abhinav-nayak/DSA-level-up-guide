class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # input is sorted and we are finding a value in it.
        # This hints towards binary search approach.
        searchIndex=-1

        l, r=0, len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target<nums[m]:
                # target is in left half
                r=m-1
            elif target>nums[m]:
                # target is in right half
                l=m+1
            else:
                # success: found the target
                searchIndex=m
                break
        
        return searchIndex

# Time complexity: O(log n)
# Space complexity: O(1)