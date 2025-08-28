# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # This is an extension of merge 2 sorted list problem.
        # Divide and conquer approach can be used. Divide till we reach 2 lists and merge them.
        # Perform this operation until all lists are merged

        return self.divide(lists, 0, len(lists)-1)
    
    def divide(self, lists: List[Optional[ListNode]], l: int, r: int)->Optional[ListNode]:
        if l>r:
            return None
        if l==r:
            return lists[l]

        mid = (l+r)//2
        left=self.divide(lists, l, mid)
        right=self.divide(lists, mid+1, r)

        # conquer by merging 2 lists
        return self.merge(left, right)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode])->Optional[ListNode]:
        """
        Merge 2 sorted linked lists
        """
        dummyHead=ListNode()
        prev=dummyHead
        while l1 and l2:
            if l1.val<=l2.val:
                prev.next=l1
                prev=l1
                l1=l1.next
            else:
                prev.next=l2
                prev=l2
                l2=l2.next
        
        if l1:
            prev.next=l1
        if l2:
            prev.next=l2
        return dummyHead.next

# Time complexity: O(n*logk)
# Space complexity: O(log k)
# where n is total number of nodes across k lists and k is the number of lists