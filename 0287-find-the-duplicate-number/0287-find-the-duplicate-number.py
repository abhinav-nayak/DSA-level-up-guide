class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # If we were allowed to modify nums, we could have used the given inout array itself as hash set
        # without taking extra space. For index=each value we could have gone and marked the value
        # negative. If at all we encounter a negative number again, that means we found the duplicate.
        # But since we cannot modify the inout array, there is another non-intuitive solution as described
        # below:
        # There are 2 challenges in this solution:
        # Challenge 1: Identifying it is a linked list cycle problem. If we consider each element in
        # input array as pointer to next element, then a cycle will be formed.
        # We can use Floyd's algorithm (using fast-slow pointers) to detect a cycle.
        # Now, the start of the cycle is the element that is duplicated.
        # Challenge 2: Finding the start of cycle. You will have fast and slow pointers which you will
        # use to detect a cycle. Once you detect a cycle, start moving the existing slow pointer one step
        # at a time. At the same time take another slow pointer which alos moves one step at a time but
        # it starts from head of linked list. The node where these 2 slow pointers meet will be the
        # start of the cycle. This is the element that has been duplicated.

        # Step 1: Detect linked list cycle
        slow,fast = 0,0
        while fast<len(nums):
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                # cycle detected
                break
        
        # Step 2: Find the start of the cycle
        slow2=0
        while slow2<len(nums):
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow
        
        return 0

# Time complexity: O(n)
# Space complexity: O(1)