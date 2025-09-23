class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Total number of disconnected components are the total number of islands. Calculate area of each island.
        Definition of connected graph is we should be able to reach each element from every element. So, from one element '1' all the other 
        1's we can visit will be one connected component (aka one island).
        This is a kind of 'grid/ matrix problem with references with elements at top, bottom, left and right or connectivity across cells'.
        This is a hint that graph can be used.
        """
        max_area = 0
        m, n = len(grid), len(grid[0])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int, area: int):
            """
            DFS traversal to calculate area
            """
            if r not in range(m) or c not in range(n) or grid[r][c] == 0:
                # Water found in this direction, we can return with 0 area
                return 0
            
            # Explore all other directions and calculate area
            grid[r][c] = 0
            area += 1
            for dr, dc in directions:
                area += dfs(r+dr, c+dc, 0)
            return area

        # Iterate through all elements of the grid and calculate area of each island by using DFS traversal.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island_area = dfs(i, j, 0)
                    max_area = island_area if island_area > max_area else max_area
        
        return max_area