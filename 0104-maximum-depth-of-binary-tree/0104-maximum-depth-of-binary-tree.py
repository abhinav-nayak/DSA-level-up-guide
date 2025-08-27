# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Since we have to find max depth of left sub-tree and right-subtree recursively,
        # we can think of Depth First Search (DFS) traversal.
        # Post order traversal can be used

        # Base condition: if node is NULL, return max depth as 0
        if not root:
            return 0
        
        leftMaxDepth=self.maxDepth(root.left)
        rightMaxDepth=self.maxDepth(root.right)
        return 1+max(leftMaxDepth, rightMaxDepth)

# Time complexity: O(n)
# Space complexity: O(n) - for recursion stack