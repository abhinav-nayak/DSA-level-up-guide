from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Pattern: monotonically decreasing queue
        # Always make sure queue is maintained in decreasing order.

        # Queue to store index
        q=deque()

        l, r = 0,0
        output=[]
        while r<len(nums):
            # While inserting if the number being inserted is bigger then keep popping
            # till it is in decreasing order and then insert.
            # If the number being inserted in smaller then directly insert.
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            if r-l+1==k:
                # window is valid, update output
                output.append(nums[q[0]])
                l+=1

                # if window has crossed element at q[0], pop from left side
                if l>q[0]:
                    q.popleft()

            r+=1

        return output

# Time complexity: O(n)
# Space complexity: O(n)