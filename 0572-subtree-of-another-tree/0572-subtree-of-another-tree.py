# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we can traverse the root tree and at each node check if root tree and sub-tree as same
        # this is extension of 'Same Tree' problem.

        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode])->bool:
        """
        check if the provided 2 trees are same
        """
        if not root and not subRoot:
            return True
        if (root and subRoot) and (root.val==subRoot.val):
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        else:
            return False

        