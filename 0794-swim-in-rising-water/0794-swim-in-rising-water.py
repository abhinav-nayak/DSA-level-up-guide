import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        If you consider each cell in the grid as a node. Water can flow from one cell to another
        based on elevation. So, each node is linked to other nodes in a random i.e., 
        non-hierarchical order. This is a hint that it can be solved using graphs.
        We can observe that the maximum elevation value along the path determines the time taken 
        for that path. Therefore, we need to find the path where the maximum elevation is 
        minimized. Can you think of an algorithm to find such a path from the source (0, 0) to 
        the destination (n - 1, n - 1)?
        Dijkstra's algorithm can help here. But, we need minor modification.
        Modified Dijkstra's algorithm:
        1. Add source node to min heap. Min heap stores a tuple: (max distance from 
        source, node).
        In normal Dijkstra's we store distacne from source, here we are modifying it to store 
        max distance from source.
        2. Till the time heap is non-empty:
        (i) Pop a node from min-heap (this way we always pick the node with shortest path)
        (ii) if popped node is not visited: Mark it as visited. Push non-visited neighbours to 
        the min heap. If popped node is visited: ignore.
        3. Once heap is empty, check if all nodes are visited. If all nodes are not visited, then
        all nodes cannot be reached.
        """
        # No need to form adjacency list here as we know the neighbours:
        # grid[i][j] has neighbours: grid[i+1][j], grid[i-1][j], grid[i][j+1], grid[i][j-1]
        # if i and j are in bounds.
        
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # hash set to keep track of visited nodes
        visited = set()

        # min heap for Dijkstra's algorithm
        min_heap = [(grid[0][0], 0, 0)]

        # var to keep track of max elevation along the minimum elevation path
        max_dist = 0

        while min_heap:
            pmax, pr, pc =  heapq.heappop(min_heap)
            # if node is visited, then ignore
            if (pr, pc) in visited:
                continue

            # mark node as visited, recalculate the max distance along this path
            visited.add((pr, pc))

            max_dist = max(max_dist, pmax)

            if pr==n-1 and pc==n-1:
                return max_dist

            # add neighbours to heap
            for dr, dc in directions:
                if 0<=pr+dr<n and 0<=pc+dc<n:
                    if (pr+dr, pc+dc) not in visited:
                        heapq.heappush(min_heap, (max(max_dist, grid[pr+dr][pc+dc]), pr+dr, pc+dc))
        
        return max_dist

# Time complexity: O(n^2 log(n))
# Space complexity: O(n^2)
