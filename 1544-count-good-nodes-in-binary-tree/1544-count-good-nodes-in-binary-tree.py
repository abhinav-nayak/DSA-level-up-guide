# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # since we have to calculate the number of good nodes, we have to visit all nodes for sure.
        # And while visiting each node, we want to know the max value from root till that node.
        # So, we can use post-order DFS traversal and store max value in each recursion stack.

        # nonlocal variable to store result
        goodNodeCount=0

        def dfsTraversal(root: TreeNode, maxTillNow: int):
            """
            Method to iterate bianry tree adn calculate the number of good nodes.
            Post order DFS traversal is used.
            """
            nonlocal goodNodeCount

            if not root:
                return
            
            # update maxTillNow variable as we traverse the tree
            if root.val>maxTillNow:
                maxTillNow=root.val
            
            dfsTraversal(root.left, maxTillNow)
            dfsTraversal(root.right, maxTillNow)

            # check if node is a good node by comparing with max value till now
            if root.val>=maxTillNow:
                goodNodeCount+=1
        
        dfsTraversal(root, float("-inf"))
        return goodNodeCount

# Time complexity: O(n)
# Space complexity: O(n) - for recursion