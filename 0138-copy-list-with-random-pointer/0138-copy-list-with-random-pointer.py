"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Pass 1: create new nodes + create a hash map of old to new node
        oldToNewNodeMap=dict()
        oldToNewNodeMap[None]=None
        # dummy node for new linked list
        dummyHead=Node(0)
        prev=dummyHead
        curr=head
        while curr:
            node=Node(curr.val)
            oldToNewNodeMap[curr]=node
            prev.next=node
            prev=node
            curr=curr.next
        prev.next=None

        # Pass 2: using hash map, set random pointers of new linked list
        while head:
            oldToNewNodeMap[head].random= oldToNewNodeMap[head.random]
            head=head.next
        
        return dummyHead.next

# Time complexity: O(n)
# Space complexity: O(n)