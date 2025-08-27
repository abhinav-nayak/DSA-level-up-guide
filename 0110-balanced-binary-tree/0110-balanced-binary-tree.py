# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # For each node, calculate the height of left and right sub-tree recursively.
        # If the difference between height of left subtree and right subtree is greater than one
        # for any node, then the tree is not height balanced.

        balanced=True

        # Since we need to calculate height of each node recursively, we can use post-order traversal
        def postOrderTraversal(root: TreeNode) -> int:
            nonlocal balanced

            if not root or not balanced:
                return 0
            
            leftHeight=postOrderTraversal(root.left)
            rightHeight=postOrderTraversal(root.right)

            if abs(leftHeight-rightHeight)>1:
                balanced=False
            return 1+max(leftHeight, rightHeight)

        postOrderTraversal(root)
        
        return balanced

# Time complexity: O(n)
# Space complexity: O(h) - for recursion stack
#                   Best case (balanced tree): O(log(n))
#                   Worst case (degenerate tree): O(n)
# Where n is the number of nodes in the tree and h is the height of the tree.
        