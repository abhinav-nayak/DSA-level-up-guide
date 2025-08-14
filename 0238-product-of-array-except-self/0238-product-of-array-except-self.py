class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # list where each element is product of elements on left
        left=[]
        leftProduct=1
        for n in nums:
            left.append(leftProduct)
            leftProduct *= n
        print("Left array: ", left)

        # list where each element is product of elements on right
        right=[1]*len(nums)
        rightProduct=1
        for i in range(len(nums)-1, -1, -1):
            right[i] = rightProduct
            rightProduct *= nums[i]
        print("Right array: ", right)
        
        # Multiple each index left and right to get the result
        result=[]
        for i in range(0, len(nums)):
            result.append(left[i]*right[i])
        
        return result

# Time complexity: O(n)
# Space complexity: O(n)