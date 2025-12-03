class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Using tabulation DP implementation technique
        # only 2 pointers are enough for tabulation method, making it space efficient
        cost1, cost2 = cost[len(cost)-2], cost[len(cost)-1]
        for i in range(len(cost)-3, -1, -1):
            temp = cost1
            cost1 = cost[i] + min(cost1, cost2)
            cost2 = temp
        return min(cost1, cost2)
