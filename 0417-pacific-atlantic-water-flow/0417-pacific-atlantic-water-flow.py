class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        This is a kind of 'grid/ matrix problem with references to elements at top, left, right 
        and down'. This is a hint that problem can be solved using graph.
        Imagine the cells through which water can flow as connected nodes.
        Basically from each cell we need to search a path to both oceans. DFS is a good approach.
        But performing DFS from each cell is inefficient. Instead of starting DFS from each cell,
        if we start DFS from boundary cells of both oceans and keep track of visited nodes in hash
        sets (one hash set per ocean), then the cells that are in both these hash sets are the cells
        from which water can flow to both oceans
        """
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # Sets to keep track of visited nodes for each ocean during DFS.
        pacific_set, atlantic_set = set(), set()

        def dfs(row: int, col: int, beach_set: set, height: int):
            """
            height is height of previous cell
            """
            if row not in range(rows) or col not in range(cols) or (row, col) in beach_set or heights[row][col] < height:
                return
            
            beach_set.add((row, col))
            for dr, dc in directions:
                dfs(row+dr, col+dc, beach_set, heights[row][col])


        # Perform DFS from top and bottom boundary cells
        for c in range(cols):
            dfs(0, c, pacific_set, heights[0][c])
            dfs(rows-1, c, atlantic_set, heights[rows-1][c])
        
        # Perform DFS from left and right boundary cells
        for r in range(rows):
            dfs(r, 0, pacific_set, heights[r][0])
            dfs(r, cols-1, atlantic_set, heights[r][cols-1])
        
        # Check for elements present in both sets
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    result.append([r, c])
        
        return result

# Time complexity: O(m*n)
# Space complexity: O(m*n)
# where m is the number of rows and n is the number of columns in the grid
