from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # The last element at each level of level order traversal will be the right side view.
        # This is an extension of level order traversal problem.
        # we can achieve level order traversal or breadth first search using a queue.
        # Inserting root node into the queue. Dequeue from the queue,
        # when popping print the node and enqueue its left and right children back into the queue.
        # Repeat this till you cover the entire tree and queue is empty.

        rightSideView = []
        q = deque()

        # Initialize the queue with root node
        if root:
            q.append(root)
        
        while q:
            # length of queue will help us identify the number of nodes at a particular level
            noOfNodesAtCurrentLevel=len(q)

            # pop all elmeents at current level and enqueue it's children
            for i in range(noOfNodesAtCurrentLevel):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # at end of for loop, node is the last element of current level
            rightSideView.append(node.val)
                
        return rightSideView

# Time complexity: O(n)
# Space complexity: O(n)