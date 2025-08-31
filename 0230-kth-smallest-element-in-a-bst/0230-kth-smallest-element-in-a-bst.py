# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder DFS traversal of Binary Search Tree will always be in sorted order.
        # We can use iterative in-order traversal approach to traverse the BST and return the
        # kth smallest element.
        
        # recursive method using in-build recursion stack.
        # For iterative approach, we need to use a stack manually.
        stack = []
        curr = root

        while curr or stack:
            # keep pushing nodes to stack till you reach left most None node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # pop node from stack and print value - inorder traversal
            curr = stack.pop()

            k -= 1
            if k==0:
                return curr.val
            
            curr = curr.right

# Time complexity: O(n)
# Space complexity: O(n)