# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # If it was not mentioned as linked list problem, still better to use linked list
        # as changing pointers is easy than shifting elements in array.

        # concept of lead-lag pointers can be used here.
        # create a dummy node which points to head for prev
        dummy=ListNode(next=head)
        lead,lag = head,dummy

        # move lead pointer n position ahead
        while n>0:
            lead=lead.next
            n-=1

        # move both lead and lag pointers by one step till lead reaches end
        while lead:
            lead=lead.next
            lag=lag.next
        
        # Now, lag is one node behind the element to be deleted
        lag.next=lag.next.next
        del lag

        return dummy.next

# Time complexity: O(n)
# Space complexity: O(1)