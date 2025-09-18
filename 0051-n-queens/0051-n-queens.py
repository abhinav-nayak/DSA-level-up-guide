class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Since we need to find 'all distinct solutions', we can use backtracking
        result = []

        # In each row only 1 queen will be there, and our recursive dfs method will search a posiiton for each row.
        # So, no need to keep track of invalid rows.
        # hash set to keep track of invalid columns
        cols_set = set()
        # hash set to keep track of invlid positive diagonal. Hint: along every positive diagonal r+c remains constant.
        pos_diagonal_set = set()
        # hash set to keep track of invalid negative diagonal. Hint: along every negative diagonal r-c remains constant.
        neg_diagonal_set = set()
        
        # Initialise a possible solution with all 0's
        self.solution = [["." for _ in range(n)] for _ in range(n)]

        def dfs(i: int):
            """
            i: row number of chess board for which we are finding queen
            """
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
                # If the position (i, j) is invalid, skip it
                if j in cols_set or i+j in pos_diagonal_set or i-j in neg_diagonal_set:
                    continue

                print("Proceeding with position: ", i, ", ", j)
                # Queen can be placed at (i, j)
                # Due to placement of this queen, mark new invalid positions so that queens won't clash
                cols_set.add(j)
                pos_diagonal_set.add(i+j)
                neg_diagonal_set.add(i-j)
                self.solution[i][j] = "Q"
                # move forward to find next row queen position
                dfs(i+1)
                # backtrack by de-selecting the prev choice and reverting marked invalid positions
                cols_set.remove(j)
                pos_diagonal_set.remove(i+j)
                neg_diagonal_set.remove(i-j)
                self.solution[i][j] = "."                    

        dfs(0)
        return result
        