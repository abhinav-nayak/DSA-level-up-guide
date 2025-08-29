# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If the current node's value is greater than p and less than q, then current node is LCA.
        # Also, if current node is equal to p or q, then also current node is LCA.
        # If both p and q are less than current node, search for LCA is left sub-tree.
        # If both p and q are greater than current node, search for LCA in right sub-tree.

        # Iterative method has better space complexity: O(1)

        # base condition 1: if p is in left sub-tree and q is in right sub-tree (or vice versa),
        # then current node is LCA
        # base condition 2: if p or q is root, then that node itself is LCA
        if (min(p.val, q.val) < root.val < max(p.val, q.val)) or (p==root or q==root):
            return root

        if p.val<root.val and q.val<root.val:
            # LCA is in left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If not, LCA is in right subtree
        return self.lowestCommonAncestor(root.right, p, q)

# TIme complexity: O(h)
# Space complexity: O(h)
# where h is the height of the tree
# h is logn for balanced tree and h=n for skewed tree