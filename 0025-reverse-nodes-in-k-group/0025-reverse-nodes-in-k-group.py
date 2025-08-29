# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Iterate through the list using lead-lag pointers.
        # lead-lag pointers should have a distance of k between them.
        # Once lead-lag pointers have a distance k between them, reverse the sub-list.

        dummyHead=ListNode(next=head)
        lead, lag = head, head
        prev = dummyHead
        while lead:
            # move lead pointer k steps ahead
            n=k
            while n>0 and lead:
                lead=lead.next
                n-=1
            
            if n==0:
                # we have found a sublist of length k. Now, reverse them.
                prev2=None
                nextPrev=lag
                while lag != lead:
                    nextt=lag.next
                    lag.next=prev2
                    prev2=lag
                    lag=nextt
                
                prev.next=prev2
                prev=nextPrev
            elif not lead:
                # we are left with a sublist whose length is less than k, no need to reverse
                prev.next=lag

        return dummyHead.next

# Time complexity: O(n)
# Space complexity: O(1)