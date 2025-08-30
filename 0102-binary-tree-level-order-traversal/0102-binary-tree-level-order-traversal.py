from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we can achieve level order traversal or breadth first search using a queue.
        # Inserting root node into the queue. Dequeue from the queue,
        # when popping print the node and enqueue its left and right children back into the queue.
        # Repeat this till you cover the entire tree and queue is empty.

        q=deque()
        levelOrderResult=[]

        # initialize the queue with root
        if root:
            q.append(root)

        while q:
            # length of queue will help us identify the number of nodes at a particular level
            noOfNodesInLevel=len(q)

            currentLevelResult=[]
            for i in range(noOfNodesInLevel):
                node = q.popleft()
                currentLevelResult.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # store the result of current level
            levelOrderResult.append(currentLevelResult)
        
        return levelOrderResult

# Time complexity: O(n)
# Space complexity: O(n)        