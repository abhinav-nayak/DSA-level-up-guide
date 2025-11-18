class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        This is like 'multiple nodes with non-hierarchical relation' kind of problem. So, this can be solved
        using graph.
        Initial thought is that since it is a minimum distance kind of problem we can use Dijkstra's
        algorithm. But there is another shortest path algorithm which handles K stops use-case intuitively
        and is more efficient.
        The algorithm is Bellman-Ford algorithm. NOTE: Bellman-Ford handles negative weight as well unlike 
        Dijkstra's algorithm.
        Bellman ford algorithm is different from traditional BFS. Here, we kind of perform BFS but iterate
        through every edge in each iteration.
        How bellamn ford algorithm works:
        1. Create an array 'prices' where index denotes the node and value denotes the price to reach that 
        node. Initialize with infinity value for all nodes except source. For source it is 0.
        2. If we can have at max K stops, then we need to perform BFS K+1 iterations.
        In every iteration:
        (i) Create a copy of prices array called 'temp_prices'.
        (ii) Iterate through every edge:
        - if prices array value for source node is infinity, skip it. As it indicates it is not an immediate 
        adjacent neighbour to perform BFS.
        - If price till source + price from source to dest is less than value in temp_prices, then update
        temp_prices with cheaper price.
        NOTE: iterating through every edge instead of just adjacent edges like traditional BFS, makes coding
        and readability easy. Time complexity is remains same. So, having more readable code at the cost of
        slight performance decrease is acceptable at times.
        NOTE: Since we are iterating through every edge and reading its prices, changing the prices array 
        in between iterations overrides few values. Hence, a temp_prices array is used.
        (iii) At the end of every iteration, assign value of temp_prices to prices array.
        """
        # Step 1: Create prices array
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0

        # Step 2: Perform BFS K+1 times
        for _ in range(k+1):
            temp_prices = prices.copy() # performs shallow copy
            for s,d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            prices = temp_prices
        
        return -1 if prices[dst] == float("inf") else prices[dst]

# Time complexity: O(n+(m∗k))
# Space complexity: O(n)
# Where n is the number of cities, m is the number of flights and k is the number of stops.