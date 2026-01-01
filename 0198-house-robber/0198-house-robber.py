class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Total amount of money that can be robbed till the ith house = max(total amount of money that can
        be robbed till (i-2)th house + money present at ith house, total amount of money that can be 
        robbed till (i-1)th house).
        This satisifes optimal sub-structure (i.e., the problem is recursive). Also, to calculate at ith
        house we need to to know (i-2)th value and to calculate at (i-1)th house also we need (i-2)th
        value. So, this satisifes overlapping sub-problem. This is similar to Fibonacci series pattern
        as there is dependency on previous 2 values. Hence, this can be solved using 1D Dynamic 
        Programming.
        With the above mentioned logic, this problem can be solved using Memoization as well as
        Tabulation technique. Tabulation requires only 2 pointers hence it is space efficient.
        """
        # Initialize first and second pointers required for Tabulation method.
        first = nums[0]
        if len(nums) == 1:
            return first
        second = max(first, nums[1])

        # Iterate all houses and calculate the total amount that can be robbed.
        for i in range(2, len(nums)):
            temp = max(first+nums[i], second)
            first = second
            second= temp
        
        return max(first, second)

# Time complexity: O(n)
# Space complexity: O(1)