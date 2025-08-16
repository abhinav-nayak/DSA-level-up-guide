class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Every element is dependent on next element to know if it can extend
        # for area calculation. Hence, we can think of stack.

        maxArea=0

        # stack to store: (<starting index for that height>, <height>)
        stack=[]
        for i, height in enumerate(heights):
            startIndex=i
            while stack and height<stack[-1][1]:
                # case where we cannot extend anymore
                lastPoppedIndex=stack[-1][0]
                area=(i-lastPoppedIndex)*stack[-1][1]
                maxArea=area if area>maxArea else maxArea
                stack.pop()
                startIndex=lastPoppedIndex

            # Possible of extending for area calculation               
            stack.append((startIndex, height))
        
        # Now stack is in increasing order only
        while stack:
            area=(len(heights)-stack[-1][0])*stack[-1][1]
            maxArea=area if area>maxArea else maxArea
            stack.pop()            
        
        return maxArea

# Time complexity: O(n)
# Space complexity: O(n)