# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # We have to explore all paths and hence we can use DFS traversal.
        # Post order traversal can be used as it is easy to calculate path sum of leaf nodes
        # and then move upwards by propogating the better path.

        # variable to store max path sum
        self.maximumPathSum = float("-inf")

        def postOrder(curr: Optional[TreeNode]) -> int:
            """
            Perform post order traversal and return back the max sum of different paths
            """
            if not curr:
                return 0
            
            maxLeft = postOrder(curr.left)
            maxRight = postOrder(curr.right)

            # For each node calculate:
            # max path sum of left-subtree + max path sum of right sub-tree + current node value.
            # It is not necessary that we add all values. If some path is negative, we can exclude.
            summ = max(maxLeft, 0) + curr.val + max(maxRight, 0)

            self.maximumPathSum = max(summ, self.maximumPathSum)

            # while returning to parent node, select better path sum which parent node can use
            return curr.val + max(max(maxLeft, 0), max(maxRight, 0))
        
        postOrder(root)

        return self.maximumPathSum

# Time complexity: O(n)
# Space complexity: O(h) -> O(n) for worst case
#                        -> O(log n) for best case