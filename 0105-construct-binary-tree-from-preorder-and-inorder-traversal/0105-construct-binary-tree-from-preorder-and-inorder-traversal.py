# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Pre-order traversal: root -> left -> right
        # So, in pre-order traversal the first node is root.
        # Now, if we find this first node in in-order tarversal (in-order traversal is left -> root -> right),
        # all nodes to left of it in in-order traversal will be in left sub-tree and all nodes to right of it
        # will be on the right sub-tree.
        # Recursively, we can run this logic to figure out which nodes will be on left sub-tree and which ones
        # on right sub-tree and construct a binary tree.

        # Hash map can be used to find out the nodes in in-order traversal.
        hashMap = dict()
        for i, n in enumerate(inorder):
            hashMap[n] = i
        
        def dfs(preorder: List[int], inorderLeft: int, inorderRight: int) -> Optional[TreeNode]:
            if len(preorder) == 0:
                return None

            # Firstnode in preorder is root always
            root = TreeNode(val=preorder[0])

            if len(preorder) == 1:
                return root

            # Find this node in inorder traversal, so that we can decide which nodes will be on left sub-tree and
            # which ones on the right sub-tree.
            mid = hashMap[preorder[0]]

            preorderMid = mid-inorderLeft
            root.left = dfs(preorder[1 : preorderMid+1], inorderLeft, mid-1)
            root.right = dfs(preorder[preorderMid+1 : preorderMid+inorderRight-mid+1], mid+1, inorderRight)
            return root
        
        return dfs(preorder, 0, len(inorder)-1)
        