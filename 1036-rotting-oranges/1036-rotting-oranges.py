from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        This is a kind of 'grid/ matrix problem with references to elements at top, left, right 
        and down'. This is a hint that problem can be solved using graph.
        We can imagine oranges to be nodes in graph.
        Every minute all neighbouring elements of a rotten orange are affected. This is nothing
        but BFS traversal, every minute every level gets affected. But, there can be more than 1
        rotten orange at every level (i.e., every minute). That means there are more than 1 source
        and this is a hint that multi-source BFS can be used.
        """
        m, n = len(grid), len(grid[0])
        self.no_of_oranges, self.no_of_rotten_oranges = 0, 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def addNeighbor(nr: int, nc: int):
            # check for out of bounds
            if nr not in range(m) or nc not in range(n) or grid[nr][nc]==0 or (nr, nc) in visited:
                return
            # mark as visited and append to queue
            visited.add((nr, nc))
            q.append((nr, nc))
            self.no_of_rotten_oranges += 1

        # initialize queue for BFS traversal
        q = deque()

        # hash set to keep track of visited nodes
        visited = set()

        # For multi source BFS: add all sources to queue first
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                    self.no_of_rotten_oranges += 1
                self.no_of_oranges += 1
        
        # perform BFS traversal
        t = 0
        while q:
            if self.no_of_rotten_oranges == self.no_of_oranges:
                return t

            # 1 level = 1 minute. So, analyse level by level
            oranges_curr_level = len(q)
            for _ in range(oranges_curr_level):
                r, c = q.popleft()
                for dr, dc in directions:
                    addNeighbor(r+dr, c+dc)

            # after each level is processed, increment time
            t += 1

        if self.no_of_rotten_oranges == self.no_of_oranges:
            return t
        return -1