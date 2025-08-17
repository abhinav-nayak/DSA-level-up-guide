class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # This is a type of 'minimum/ maximum feasible value' kind of problem.
        # Hence, we can think of binary search approach.
        # Important thing to note here is that, we do not appply binary search on input data,
        # we find the the possible value range for k and then apply binary search to this range.

        # Find the range of k
        # Minimum banana that can be eatenin 1 hour = 1
        # Maximum banana that can be eaten in 1 hr = max(piles)
        maxBananas=0
        for p in piles:
            maxBananas=p if p>maxBananas else maxBananas
        # So, now we know range of k: [1, maxBananas] and obviously this is in sorted order.

        minK=maxBananas
        # Apply binary search logic for range of k and find the min feasible value of k.
        l,r = 1,maxBananas
        while l<=r:
            mid=(l+r)//2

            # with k=mid, check how many hours are needed to eat all bananas
            t=0
            for p in piles:
                t=t + p//mid
                if p%mid>0:
                    t+=1

            if t<=h:
                # Time taken to eat with k=mid speed is less than h hours.
                # we can search for lower value of k such that time is still satisifed
                minK=mid if mid<minK else minK
                r=mid-1
            else:
                # Time taken if more than whats required, so koko needs to eat more faster.
                # we can search for higher value of k such that time is still satisified.
                l=mid+1
        
        return minK

# Time complexity: O(log(max val in piles)*n)
# Space complexity: O(1)