class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # In reality this is a two pointer problem than sliding window

        maxProfit=0
        if len(prices)==1:
            return maxProfit
        
        # initialise 2 pointers, 'b' for buying and 's' for selling
        b, s=0, 1
        while s<len(prices):
            if prices[s]<prices[b]:
                # since selling price is less, we can buy stock at this price
                b=s
                s+=1
            else:
                # calulate profit and move sforward to check for better profits
                profit=prices[s]-prices[b]
                maxProfit=profit if profit>maxProfit else maxProfit
                s+=1
        
        return maxProfit

# Time complexity: O(n)
# Space comlexity: O(1)