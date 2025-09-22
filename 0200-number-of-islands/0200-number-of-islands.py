from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Total number of disconnected components are the total number of islands.
        Definition of connected graph is we should be able to reach each element from every element. So, from one element '1' all the other 
        1's we can visit will be one connected component (aka one island).
        This is a kind of 'grid/ matrix problem with references with elements at top, bottom, left and right or connectivity across cells'.
        This is a hint that graph can be used.
        """
        self.island_count = 0

        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # The following DFS method works. Trying out BFS next.
        """
        def dfs(r: int, c: int):
            # We can keep hash set to keep track of visited nodes. But, here once visited we will mark it as 0, avoiding hash set.
            if r not in range(rows) or c not in range(cols) or grid[r][c] == "0":
                return
            
            # Mark the element as visited and explore other paths.
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)


        # Iterate through all elements of the grid. Whenever you find one "1", start DFS search to cover all other connected 1's.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    self.island_count += 1
        """

        # Trying BFS approach below.
        def bfs(x: int, y: int):
            # Using queue for BFS
            q = deque()
            # Mark element as visited and append to queue.
            grid[x][y] = "0"
            q.append((x, y))
            while q:
                # NOTE: if we change 'popleft' to just 'pop', this becomes iterative DFS implementation.
                r, c= q.popleft()
                for dr, dc in directions:
                    if r+dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc] == "1":
                        grid[r+dr][c+dc] = "0"
                        q.append((r+dr, c+dc))



        # Iterate through all elements of the grid. Whenever you find one "1", start DFS search to cover all other connected 1's.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    self.island_count += 1
        
        return self.island_count

# Time complexity: O(m*n)
# Space complexity: O(m*n)
# where m is the number of rows and n is the number of columns in the grid.