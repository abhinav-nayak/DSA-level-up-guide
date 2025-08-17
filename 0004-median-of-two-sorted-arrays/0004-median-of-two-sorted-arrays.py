class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Both arrays are sorted and time complexity reqirement is in log.
        # Hence, binary search approach.

        # Sorting and then doing binary search will take more time complexity.
        # Basically, if we know partition in array 1 as well as array 2, such that
        # all elements on left of partition on both arrays belong to left half of merged array
        # and rest belong to right half, then we will know the elements at the half point of merged
        # array. Once we know the elements at center of merged array, we can directly calculate median.
        
        # Always perform binary search on smaller array.
        # Else we might end up in index out of bounds error. And also it is more efficient.
        if len(nums2)<len(nums1):
            nums1, nums2 = nums2, nums1

        total=len(nums1)+len(nums2)
        half=total//2 if total%2==0 else (total+1)//2
        median=0

        l,r = 0,len(nums1)
        while l<=r:
            # NOTE: partition indicates number of elements, not index
            partition1=(l+r)//2
            partition2=half-partition1


            left1  = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            right1 = nums1[partition1]     if partition1 < len(nums1) else float("inf")

            left2  = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            right2 = nums2[partition2]     if partition2 < len(nums2) else float("inf")
            if left1<=right2 and left2<=right1:
                # we have found the boundary elements near partition of both array.
                # Calculate median
                if total%2==0:
                    median=(max(left1, left2)+min(right1, right2))/2
                    break
                else:
                    median=max(left1, left2)
                    break
            
            # Adjust the partition to make sure you have found the correct left and right halfs of merged array
            if right1<left2:
                l=partition1+1
            elif right2<left1:
                r=partition1-1
        
        return median

# Time complexity: O(log(min(n, m)))
# Space complexity: O(1)
# where m is length of nums1 and n is length of nums2