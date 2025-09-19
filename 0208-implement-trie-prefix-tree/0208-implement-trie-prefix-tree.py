class TrieNode:
    def __init__(self):
        # Trie node has 2 components:
        # (i) Hash map to map character with it's trie node
        # (ii) Bool flag to indicate a valid word
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        # Use tries for operations on large number of strings especially prefix matching. It is the most efficient for prefix matching
        # and hence trie is also called prefix tree.
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        # Iterate through given word one character at a time and insert TrieNode if required.
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        # Mark it as valid word
        curr.end_of_word = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        # Iterate through given word one character at a time and check if it is present in children. At the end check if it is a valid word.
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        
        return curr.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        # Iterate through given word one character at a time and check if it is present in children. No need ot check for valid word as we are
        # just checking prefix match and not perfect string match. This is the only difference between 'search' and 'startsWith' methods.
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True
        
# Time complexity: O(n)
# Space complexity: O(t)
# where n is the length of the word and t is the total number trie nodes created in the trie

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)