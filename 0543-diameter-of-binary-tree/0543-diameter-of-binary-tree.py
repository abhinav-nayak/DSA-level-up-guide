# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This looks like extension of previous problem: Max depth of binary tree
        # For each node if we find the max height of left and right subtrees and add them we get
        # the diameter of binary tree.

        # Since we have to find the height of left and right subtree and then add them, we can use
        # Post-order DFS traversal

        # use nonlocal keyword to store the result during recursion and create an inner function
        maxDiameter=0

        # inner fucntion for DFS post-order traversal
        def postOrderDFS(root: TreeNode):
            # base condition: leaf nodes have height 0
            if not root:
                return 0
            
            maxLeftHeight=postOrderDFS(root.left)
            maxRightHeight=postOrderDFS(root.right)
            diameter=maxLeftHeight+maxRightHeight

            nonlocal maxDiameter
            maxDiameter=max(diameter, maxDiameter)

            return 1+max(maxLeftHeight, maxRightHeight)
        
        postOrderDFS(root)
        return maxDiameter

# Time complexity: O(n)
# Space complexity: O(h) - for recursion stack
#                   Best case (balanced tree): O(log(n))
#                   Worst case (degenerate tree): O(n)
# Where n is the number of nodes in the tree and h is the height of the tree.
