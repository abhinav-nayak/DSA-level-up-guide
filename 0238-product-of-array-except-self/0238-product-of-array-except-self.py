class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
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
        '''

        # Optimal solution with O(1) extra space
        # Same logic as above, but avoid having left and right lists
        result=[1]*len(nums)

        # enter all left array elements into result
        leftProduct=1
        for i in range(len(nums)):
            result[i] = leftProduct
            leftProduct *= nums[i]

        # multiply right array elements into reuslt on the fly
        rightProduct=1
        for i in range(len(nums)-1, -1, -1):
            result[i]=result[i]*rightProduct
            rightProduct *= nums[i]

        return result

        # Time complexity: O(n)
        # Space complexity: O(1) (excluding result array)