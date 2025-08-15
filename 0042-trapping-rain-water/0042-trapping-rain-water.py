class Solution:
    def trap(self, height: List[int]) -> int:
        # water trapped at each index = min(maxLeft, maxRight)-h[i]
        # Solution 1: Traverse once through given array and form maxLeft and maxRight arrays.
        #             Then iterate again to calculate the above formula.
        #             Space complexity: O(n). It can be reduced to O(1) by two pointers.

        # Solution 2: Converging 2 pointers. Implemented below
        # initialize two converging pointers
        l=0
        r=len(height)-1

        # initialize currently known maxLeft and maxRight
        maxLeft=height[l]
        maxRight=height[r]

        waterTrapped=0
        while l<r:
            # Move the pointer that has lesser max value.
            # This is for implicit calculation of  min(maxLeft, maxRight)-h[i]
            if maxLeft<=maxRight:
                l+=1
                water = maxLeft-height[l] if (maxLeft-height[l]) >0 else 0
                waterTrapped += water
                maxLeft = height[l] if height[l]>maxLeft else maxLeft
            else:
                r-=1
                water = maxRight-height[r] if (maxRight-height[r]) >0 else 0
                waterTrapped += water
                maxRight = height[r] if height[r]>maxRight else maxRight
        
        return waterTrapped

# Time complexity: O(n)     
# Space complexity: O(1)