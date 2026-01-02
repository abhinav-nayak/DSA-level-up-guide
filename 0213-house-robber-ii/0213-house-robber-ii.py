class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Logic for solving the problem if first and last houses were not neighbours:
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

        Logic modification if first and last houses are neighbours:
        Suppose given nums lenght is n.
        We need to consider 2 cases here:
        Case 1: Select 1st house (meaning we should not select last house): For this run the above logic
        from first house till second-to-last house.
        Case 2: Select last house (meaning skip 1st house): For this run the above logic from second house
        till the last house.
        The max of Case 1 and Case 2 is the solution for this problem.
        """
        # Corner case
        if len(nums) == 1:
            return nums[0]

        # For tabulation method initialize the two pointers
        h1, h2 = 0, 0

        # Case 1: select first house and exclude the last house
        for i in range(len(nums)-1):
            temp = max(nums[i]+h1, h2)
            h1 = h2
            h2 = temp
        res1 = h2

        # Case 2: exclude first house and select the last house
        h1, h2 = 0, 0
        for i in range(1, len(nums)):
            temp = max(nums[i]+h1, h2)
            h1 = h2
            h2 = temp
        res2 = h2

        return max(res1, res2)

# Time complexity: O(n)
# Space complexity: O(1)
