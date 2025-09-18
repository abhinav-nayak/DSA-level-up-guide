import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Since we need to find 'all distinct solutions', we can use backtracking
        result = []
        
        # Initialise a possible solution with all 0's
        self.solution = [[0 for _ in range(n)] for _ in range(n)]

        def dfs(i: int):
            """
            i: row number of chess board for which we are finding queen
            """
            def markPositionsInvalid(r: int, c: int):
                """
                r: current row number
                c: current column number
                """
                # mark the entire row as invalid
                for z in range(n):      
                    self.solution[r][z] = "."

                # mark the entire column as invalid
                for z in range(n):      
                    self.solution[z][c] = "."

                # mark the diagonals as invalid
                # process right down diagonal
                drow, dcolumn = r, c
                while 0 <= drow <n and 0 <= dcolumn < n:
                    self.solution[drow][dcolumn] = "."
                    drow += 1
                    dcolumn +=1
                # process left up diagonal
                drow, dcolumn = r, c
                while 0 <= drow <n and 0 <= dcolumn < n:
                    self.solution[drow][dcolumn] = "."
                    drow -= 1
                    dcolumn -=1
                # process right up diagonal
                drow, dcolumn = r, c
                while 0 <= drow <n and 0 <= dcolumn < n:
                    self.solution[drow][dcolumn] = "."
                    drow -= 1
                    dcolumn +=1
                # process left down diagonal         
                drow, dcolumn = r, c
                while 0 <= drow <n and 0 <= dcolumn < n:
                    self.solution[drow][dcolumn] = "."
                    drow += 1
                    dcolumn -=1
            
            # --- DFS method starts here --- #
            print("------- Searching Queen position for row: ", i, "--------")
            if i >= n:
                # We have found positions for all n queens
                # print("found solution: ", self.solution)
                soln = [""]*n
                for k in range(n):
                    soln[k] = "".join(self.solution[k])
                result.append(soln)
                return

            # Check possibility of placing queen in each of the positions in the given row
            for j in range(n):
                # print("solution: ", self.solution)
                # If the position (i, j) is valid, select posiiton (i, j)
                if self.solution[i][j] != ".":
                    print("Proceeding with position: ", i, ", ", j)
                    # Queen can be placed at (i, j)
                    soln_before_choice = copy.deepcopy(self.solution)
                    # Due to placement of this queen, mark new invalid positions so that queens won't clash
                    markPositionsInvalid(i, j)
                    self.solution[i][j] = "Q"
                    # move forward to find next row queen position
                    dfs(i+1)
                    # backtrack by de-selecting the prev choice and reverting marked invalid positions
                    self.solution = soln_before_choice

        dfs(0)
        return result
        