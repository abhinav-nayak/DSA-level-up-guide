# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node which helps in corner cases
        prev=ListNode()
        head=prev

        # readjust the links till you reach end of any one of the list
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next=list1
                prev=list1
                list1=list1.next
            else:
                prev.next=list2
                prev=list2
                list2=list2.next
        
        prev.next=list1 if list1 else list2
        return head.next
