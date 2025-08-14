class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0

        # use converging 2 pointers to find the max amount of water
        i, j=0, len(height)-1
        while i<j:
            area=(j-i)*min(height[i], height[j])
            maxArea=area if area>maxArea else maxArea

            # move the pointers thats limiting the area i.e., the smaller one
            if height[i]<height[j]:
                i += 1
            else:
                j-=1
        
        return maxArea

# Time complexity: O(n)
# Space complexity: O(1)
        