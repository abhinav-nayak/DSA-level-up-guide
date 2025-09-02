import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # This is a kind of 'find maximum or minimum value frequently' problem because on each
        # turn we choose the heaviest two stones. This is a hint to use heap.
        # Max heap can be used here.

        # Create max heap from the provided data
        stones = [stone*-1 for stone in stones]
        heapq.heapify(stones)

        # Play the game until we are left with 0 or 1 stones
        while len(stones)>1:
            # Choose heaviest 2 stones
            y = heapq.heappop(stones) * -1
            x =  heapq.heappop(stones) * -1

            # Re-insert as per game rules
            if x < y:
                heapq.heappush(stones, x-y)

        lastStoneWeight = stones[0]*-1 if len(stones)>0 else 0
        return lastStoneWeight

# Time complexity: O(nlogn)
# Space complexity: O(n)