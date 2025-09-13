class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # From every element we have to travel in all possible directions ot check if word can be formed.
        # Since, we must travel all paths, it is a hint that bcaktracking can be used.
        rows, columns = len(board), len(board[0])
        # since same element cannot be used again, keep track of visited elements
        visited = set()
        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            # checks if element at (r, c) matches required word element at i
            if r <0 or c <0 or r>=rows or c>= columns or board[r][c] != word[i] or (r, c) in visited:
                return False

            # Mark current element as visited and search for next element in all 4 directions
            visited.add((r, c))
            result = dfs(r, c-1, i+1) or dfs(r, c+1, i+1) or dfs(r-1, c, i+1) or dfs(r+1, c, i+1)
            visited.remove((r, c))
            return result

        # Starting from each element in the matrix, check if word can be formed
        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True
        
        return False

# Time complexity: O(m * 4^(n))
# Space complexity: O(n)
# where m is the total number of elements in the matrix and n is the length of the word