# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Use any DFS traversal apporach and check if all values are same

        # Performing post order traversal
        sameTree=True

        def postOrderTraversal(p: TreeNode, q: TreeNode):
            nonlocal sameTree

            if not p or not q:
                if p!=q:
                    sameTree=False
                return

            postOrderTraversal(p.left, q.left)
            postOrderTraversal(p.right, q.right)
            if p.val != q.val:
                sameTree=False
        
        postOrderTraversal(p, q)
        return sameTree
        