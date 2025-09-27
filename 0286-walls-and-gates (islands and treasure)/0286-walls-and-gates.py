from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # The commented code performs DFS traversal as a solution. But the time complexity 
        # of this is O((m*n)^2). Performing BFS would also have the same time complexity.
        # The most optimal solution lies in a variation of BFS approach: Multi-source BFS.
        # Instead of starting from land in case of normal BFS, what if we start from all
        # treasures simultaneously? This is called multi-source BFS.
        # When to use multi-source BFS: When you need the shortest distance from any one of
        # several start points to all other nodes.
        # It's more efficient than doing many separate single‐source BFS runs
        # (one from each source), since you're combining them into a single traversal.
        '''
        """
        This is a kind of 'grid/ matrix problem with references with elements at
        top, bottom, left and right or connectivity across cells'.
        This is a hint that graph can be used.
        Visualize the grid as graph. INF and 0 are vertices which can be traversed and up, down,
        left and right elements are connected. -1 is water which can be ignored in graph as they
        cannot be traversed.
        """

        # Approach 1: DFS

        INF = 2147483647
        m, n = len(grid), len(grid[0])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # Maintain a hash set to keep track of visited elements so that we don't get
        # stuck in loop in case the graph is cyclic.
        visited = set()

        # DFS traversal method to explore all paths till treasure adn return the min distance
        def dfs(r: int, c: int, dist: int) -> int:
            """
            r: current row number
            c: current column number
            dist: distance till the current node from beginning
            """
            # Base condition: if node is already visited or you find a treasure or out of bounds or found water
            if r not in range(m) or c not in range(n) or (r, c) in visited or grid[r][c] == -1:
                return INF
            if grid[r][c] == 0:
                return dist

            # Mark current node as visited
            visited.add((r, c))
            # Explore other paths in all 4 directions
            shortest_dist = INF
            for dr, dc in directions:
                treasure_dist = dfs(r+dr, c+dc, dist+1)
                shortest_dist = min(treasure_dist, shortest_dist)
            
            visited.remove((r, c))
            return shortest_dist


        # Iterate through entire grid, whenever land is encountered call dfs traversal method
        # to find the shortest distance to treasure
        for i in range(m):
            for j in range(n):
                if grid[i][j] == INF:
                    grid[i][j] = dfs(i, j, 0)
        '''

        # Approach 2: Multi-source BFS
        INF = 2147483647
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def addNodeToQueue(i: int, j: int):
            if i not in range(m) or j not in range(n) or grid[i][j]!=INF or (i, j) in visited:
                return
            visited.add((i, j))
            q.append((i, j))
            

        # In this problem, source is treasure. Add all sources to queue first.
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # Perform BFS traversal
        visited = set()
        distance = 0
        while q:
            # NOTE: at each level in BFS, all nodes are at same distance from all sources.
            # First iteration all nodes are at a distance of 1 from treasure and in next iteration
            # distance is 2 and so on
            nodes_at_curr_level = len(q)
            for _ in range(nodes_at_curr_level):
                r, c = q.popleft()
                grid[r][c] = distance
                # Mark the node as visited
                visited.add((r,c))
                # Explore  neighbours
                for dr, dc in directions:
                    addNodeToQueue(r+dr, c+dc)
                        
            # Incrment distance for next level of BFS
            distance += 1

# Time complexity: O(m*n)
# Space complexity: O(m*n)
# Where m is the number of rows and n is the number of columns in the grid
