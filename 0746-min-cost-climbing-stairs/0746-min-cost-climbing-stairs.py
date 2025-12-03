class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        We know that the min cost required to reach the top from last 2 steps is their own cost 
        (this is the base condition). Min cost to reach from a step is cost of current step + min
        (min cost from next step to reach top, min cost from next to next step to reach top).
        This satisifes optimal substructure. And if you draw the recursion tree you will see it
        satisfies overlapping solution as well. Hence, this can be solved in Dynamic Programming.
        This is similar to Fibonacci series pattern.
        With the above mentioned logic, this can be solved using Memoization and Tabulation 
        technique both. Tabulation technique requires only 2 pointers and is space efficient.
        """
        # Using tabulation DP implementation technique
        # only 2 pointers are enough for tabulation method, making it space efficient

        # min cost required to reach the top from last 2 steps is their own cost
        cost1, cost2 = cost[len(cost)-2], cost[len(cost)-1]
        for i in range(len(cost)-3, -1, -1):
            # Min cost to reach from a step is cost of current step + min(min cost from next step 
            # to reach top, min cost from next to next step to reach top).
            temp = cost1
            cost1 = cost[i] + min(cost1, cost2)
            cost2 = temp
        return min(cost1, cost2)

# Time complexity: O(n)
# Space complexity: O(1)
