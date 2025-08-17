class Solution:
    def findMin(self, nums: List[int]) -> int:
        # data is sorted (rotated is okay), so we can try binary search

        minElement=0

        l,r = 0,len(nums)-1
        while l<=r:
            # case when the data is already sorted
            if nums[l]<nums[r]or l==r:
                minElement=nums[l]
                break

            # reduce binary search till a point where only 2 elements are left.
            if r-l+1==2:
                # one of these elements has to be the smallest
                minElement=min(nums[l], nums[r])
                break

            mid=(l+r)//2

            if nums[l]>nums[mid]:
                # this won't happen if left half was sorted properly
                # left has that rotated part and smallest element as well
                r=mid
            elif nums[mid]>nums[r]:
                # this won't happen if right half was sorted properly
                # right part has that rotated part and smallest element as well
                l=mid
        
        return minElement

# Time complexity: O(log n)
# Space complexity: O(1)