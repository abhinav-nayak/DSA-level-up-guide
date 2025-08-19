# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # fast-slow pointers approach can be used
        slow=head
        fast=head
        # if a cycle exists then at somepoint fast and slow pointers will meet
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True

        return False

# Time complexity: O(n)
# Space complexity: O(1)