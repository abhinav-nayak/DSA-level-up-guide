# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate through both lists and add each node and keep track of carry
        carry=0
        dummyNewHead=ListNode()
        curr=dummyNewHead
        while l1 and l2:
            s=l1.val+l2.val+carry
            newNode=ListNode(val=s%10)
            curr.next=newNode
            curr=newNode
            carry=s//10

            l1=l1.next
            l2=l2.next
        
        # handle case where l1 or l2 elements are still present
        l=l1 if l1 else l2
        while l:
            s=l.val+carry
            newNode=ListNode(val=s%10)
            curr.next=newNode
            curr=newNode
            carry=s//10
            l=l.next
        
        # after adding if carry is left add new node
        if carry>0:
            newNode=ListNode(val=carry)
            curr.next=newNode
            curr=newNode

        return dummyNewHead.next

# Time complexity: O(m+n)
# Space complexity: O(1) for extra space, O(max(m, n)) for output list
# where m is length of l1 and n is length of l2