# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # To validate BST, we must traverse the entire tree and check if each node satisfies
        # the required conditions. Pre-order DFS traversal can be used here.
        # While visiting each node, we can pass the min and max value that node can have.
        # We start from root node, the min and max for root node is (-inf, inf).
        # When we move to left sub-node, the left sub-node can have values in range of:
        # (min value that parent node could have had, parent node value)
        # When we move to right sub-node, the right sub-node can have values in range of:
        # (parent node value, max value that parent node could have had)

        def preOrderTraversal(root: TreeNode, minVal: int, maxVal: int) -> bool:
            if not root:
                return True
            
            # Check if current node value is in the expected range: (minVal, maxVal)
            if root.val<=minVal or root.val>=maxVal:
                return False
            
            if not preOrderTraversal(root.left, minVal, root.val):
                return False
            if not preOrderTraversal(root.right, root.val, maxVal):
                return False
            
            # If both left sub-tree an right sub-tree are valid, then BST is valid
            return True

        # Min and max value for root: (-inf, inf)
        return preOrderTraversal(root, float("-inf"), float("inf"))

# Time complexity: O(n)
# Space complexity: O(n) -  for recursion stack