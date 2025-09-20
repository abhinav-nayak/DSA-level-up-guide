class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    # Hash table cannot be used because while searching we need to handle the case of '.'.
    # Since, we have to store multiple strings and search with '.', we can use tries. For exploring all options for '.' we can use
    # backtracking.

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        # Iterate given word one character at a time and insert into trie
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.end_of_word = True

        

    def search(self, word: str) -> bool:
        # Since word can have '.', we might have to explore all possible paths to reach a solution.
        # Hence, backtracking can be used along with trie search logic
        # Iterate through given word one character at a time. When you encounter '.' explore paths by backtracking
        def dfs(i: int, current: TrieNode) -> bool:
            """
            i is the index of the word
            """
            # base condition
            if i == len(word):
                return current.end_of_word
                
            if word[i] == ".":
                # explore paths from all children
                for c in current.children:
                    found = dfs(i+1, current.children[c])
                    if found:
                        return True
                return False
            elif word[i] in current.children:
                return dfs(i+1, current.children[word[i]])
            else:
                return False
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)