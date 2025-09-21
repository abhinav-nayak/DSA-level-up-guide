class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        # Index to map the word with the word position in given list words
        self.index = None

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Recall we had performed one word search before as part of backtracking problem. But, performing the same backtracking for n strings is 
        # inefficient. So, which other data structure is good with large strings? Which data structure helps us store multiple strings and search?
        # This is where tries come in. This is a hint that trie can be used.
        m, n = len(board), len(board[0])

        self.result = []
        # Maintain a hash set to make sure the same letter cell may not be used more than once in a word.
        visited = set()

        def dfs(r: int, c: int, current: TrieNode):
            """
            r: row number of current position in board
            c: column number of current position in board
            current: current trie node in trie
            """
            # Found a solution
            if current.end_of_word and current.index != -1:
                self.result.append(words[current.index])
                current.index = -1

            # The same letter cell may not be used more than once in a word.
            if r<0 or r>=m or c<0 or c>=n or (r, c) in visited or board[r][c] not in current.children:
                return

            if board[r][c] in current.children:
                # mark as visited and move further in all directions
                visited.add((r, c))
                dfs(r+1, c, current.children[board[r][c]])
                dfs(r-1, c, current.children[board[r][c]])
                dfs(r, c+1, current.children[board[r][c]])
                dfs(r, c-1, current.children[board[r][c]])
                visited.remove((r, c))


        # Step 1: Insert all words into a trie. Store the index of the word as well
        for i, word in enumerate(words):
            curr = self.root
            for w in word:
                if w not in curr.children:
                    curr.children[w] = TrieNode()
                curr = curr.children[w]
            curr.end_of_word = True
            curr.index = i

        # Step 2: Iterate through all elements of the given board. If element is not already visited for that word  and it is there in
        # children of current node, then mark it as visited and move further. If not, backtrack and mark as unvisited and check if other 
        # neighbouring elements are there in current node's children. Once we reach a node with end of word = True and its index is not equal to -1
        # then append to result and mark its index as -1 to prevent from adding same in the result again. 

        for i in range(m):
            for j in range(n):
                dfs(i, j, self.root)

        return self.result

# Time complexity: O(m*n*4*3^(t-1) + s)
# Space complexity: O(s)
# Where m is the number of rows, n is the number of columns, t is the maximum length of any word in the array words and 
# s is the sum of the lengths of all the words.