# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head

        # Even if it is not explicitly mentioned to use linked list, note that lot of elements are
        # getting adjusted i.e., position changed. This is easier using linked list than arrays as
        # changing pointers is easy than shifting array values.

        # Step 1: Find the half point of the linked list
        # Step 2: Reverse the second half
        # Step 3: Pick element from first half and second half alternatively
        #         and form the expected linked list

        # Step 1: best way to find half point is using fast-slow pointer
        slow,fast,prev1 = head,head,head
        while fast and fast.next:
            prev1=slow
            slow=slow.next
            fast=fast.next.next
        # disconnecting first half from second half
        prev1.next=None
        
        # you can consider 'slow' pointer as the starting node of second half
        # Step 2: Reverse the second half
        prev=None
        while slow:
            nextNode=slow.next
            slow.next=prev
            prev=slow
            slow=nextNode
        
        # now you can consider 'prev' pointer as satrting node of reversed second half
        # Step 3: Pick element from first half and second half alternatively
        first=head
        lastModified2=None
        while first and prev:
            next1=first.next
            first.next=prev
            next2=prev.next
            prev.next=next1
            first=next1
            lastModified2=prev
            prev=next2
        
        # incase of list of odd length, second half might still have elements
        if prev:
            lastModified2.next=prev

# Time complexity: O(n)
# Space complexity: O(1)