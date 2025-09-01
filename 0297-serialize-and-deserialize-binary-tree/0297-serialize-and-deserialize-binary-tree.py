# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # We can solve this using both BFS and DFS.
        # Solution 1 (using BFS): Perform BFS traversal using queue and store the sequence of nodes in
        # string.
        # Solution 2 (using DFS): Perform preorder traversal and store the sequence of nodes in string.
        # For both the above solutions:
        # (i) Keep a delimiter to separate node values in string.
        # (ii) NULL node can be represented by N or / or any other character.
        # NOTE: join and split string methods help a lot here

        # Implementing solution 2: preorder traversal
        serializedArray = []

        def dfs(curr):
            if not curr:
                serializedArray.append("/")
                return

            serializedArray.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
        
        dfs(root)
        return ",".join(serializedArray)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        serializedArray = data.split(",")

        # Index to create root
        self.preorderIndex = 0
        
        # Perform preorder traversal (same that was used while serializing)
        def dfs() -> TreeNode:
            if serializedArray[self.preorderIndex] == "/":
                self.preorderIndex += 1
                return None

            curr = TreeNode(int(serializedArray[self.preorderIndex]))
            self.preorderIndex += 1

            curr.left = dfs()
            curr.right = dfs()

            return curr
        
        return dfs()

# Time complexity: O(n) - for both serialize and deserialize
# Space complexity: O(n) - for both serialize and deserialize
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))