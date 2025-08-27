# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # since we have to swap the left and right of each node from bottom to top,
        # we can think of DFS traversal. Post-order traversal can be used because once we
        # swap the left and right sub-trees recursively, the root's left and right should be swapped.

        # Post-order traversal

        # base condition: if the node has no children, there is nothing to swap
        if (not root) or (not root.left and not root.right):
            return root
        
        leftNode=self.invertTree(root.left)
        rightNode=self.invertTree(root.right)
        root.left=rightNode
        root.right=leftNode

        return root

# Time complexity: O(n)
# Space complexity: O(n) - for recursion stack