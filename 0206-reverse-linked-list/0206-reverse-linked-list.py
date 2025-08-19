# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None

        # directly reverse the pointers
        while head:
            nextt=head.next
            head.next=prev
            prev=head
            head=nextt
        return prev

# Time complexity: O(n)
# Space complexity: O(1)
