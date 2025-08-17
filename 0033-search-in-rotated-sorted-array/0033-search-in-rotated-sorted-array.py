class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Data is sorted (rotated as well, but that's okay).
        # We can think of binary search
        l,r = 0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid

            if nums[l]<=nums[mid]:
                # left half is sorted
                if nums[l]<=target<=nums[mid]:
                    # target present in sorted left half
                    r=mid-1
                else:
                    # target can be in unsorted right half
                    l=mid+1
            elif nums[mid]<=nums[r]:
                # right half is sorted
                if nums[mid]<=target<=nums[r]:
                    # target is present in right sorted half
                    l=mid+1
                else:
                    # target is in unsorted left half
                    r=mid-1
        
        return -1

# Time complexity: O(log n)
# Space complexity: O(1)