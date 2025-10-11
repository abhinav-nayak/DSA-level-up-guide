class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        Usually grid problems, thought of backtracking or graph can come. Backtracking we
        usually use when multiple solutions are required (not always).
        This is a kind of 'grid/ matrix problem with references to elements on left/ right/
        top/bottom'. Hence, we can think of graph.
        For fidning surround regions, we will probably need some form of traversal. We can 
        think of DFS here. If we start from O's which can be surrounded, it gets tougher to 
        solve this problem. What if we think the otherway around i.e., start from cells that
        cannot be surrounded. This way problem becomes less challenging.
        Step 1: we know that all O's in boundary cannot be surrounded. From each of these 
        O's start DFS and mark those cells as T (indicating cannot be surrounded).
        Step 2: Now all remaining O's in the grid can be surrounded. So, iterate through
        entire grid and mark O's as X's (as requested in question)
        Step 3: Again iterate through entire grid and mark the T's as O's.
        """
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # hash set to keep track of visited elements
        visited = set()

        # DFS traversal implementation
        def dfs(r: int, c: int):
            if r not in range(m) or c not in range(n) or (r, c) in visited or board[r][c]!="O":
                return
            visited.add((r, c))
            board[r][c] = "T"
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        # Step 1: Perform DFS tarversal from all O's that cannot be surrounded (basically boundary)
        for row in range(m):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][n-1] == "O":
                dfs(row, n-1)

        for col in range(n):
            if board[0][col] == "O":
                dfs(0, col)
            if board[m-1][col] == "O":
                dfs(m-1, col)
        
        # Step 2: Iterate through entire board and change O -> X as remaining O's can be surrounded
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
        
        # Step 3: Again iterate through entire grid and mark the T's as O's
        for row in range(m):
            for col in range(n):
                if board[row][col] == "T":
                    board[row][col] = "O"        

# Time complexity: O(m*n)
# Space complexity: O(m*n)