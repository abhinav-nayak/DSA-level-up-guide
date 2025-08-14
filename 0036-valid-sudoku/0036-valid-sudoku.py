class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check validity of each row
        for row in board:
            # to check for duplicate elements in each row
            hashSet=set()
            for num in row:
                if num==".":
                    continue
                if num in hashSet:
                    return False
                hashSet.add(num)
        
        # check for validity of each column
        for j in range(len(board)):
            # to check for duplicate elements in each column
            hashSet=set()
            for row in board:
                if row[j]==".":
                    continue
                if row[j] in hashSet:
                    return False
                hashSet.add(row[j])
        
        # check for validity of sub-boxes
        for m in range(0, len(board), 3):
            for n in range(0, len(board), 3):
                # to check for duplicate elements in each sub-box
                hashSet=set()
                for i in range(m, m+3):
                    for j in range(n, n+3):
                        if board[i][j]==".":
                            continue
                        if board[i][j] in hashSet:
                            return False
                        hashSet.add(board[i][j])
    
        return True

        