import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # This is a kind of 'find maximum or minimum value' problem as we have to find the Kth largest
        # element in an array. This indicates that it is a heap problem. We can use min-heap.
        # Time complexity would be O(nlogk) and space complexity would be O(k).
        '''
        # The following approach works, but one teste case is exceeding time limit, maybe because of worst case time 
        # complexity of O(n^2)

        # Since we have used heap approach before, I will using another approach here i.e., Quick Select
        # algorithm. This is similar to quick sort algorithm.
        # Time complexity: O(n) - average case, O(n^2) - worst case
        # Space complexity: O(n)
        # Here, we choose a pivot point, the last element can be considered as pivot in every iteration.
        # Now, we have adjust the pivot element position such that all elements to the left of it are
        # smaller than pivot and all elements to the right of it are greater than pivot. Now, the pivot is
        # in its correct sorted position (rest of the elements are not yet sorted).
        # How will we move pivot to its correct sorted position?
        # Take two pointers 'i' (i increments in every iteration) and 'p' starting from left end.
        # In every iteration check if nums[i] <= nums[pivot]. If yes, swap nums[i] and nums[p].
        # Increment p. If nums[i] > nums[pivot], don't increment p. This makes sure that all elements until
        # pointer p is smaller than pivot.
        # When 'i' reaches pivot, swap nums[pivot] and nums[p]
        # Recursively continue this procedure in either left half or right half depending on where index k
        # from end is with respect to pivot.

        # This means, element at index k has to be returned
        # Once we find correct sorted position at index k, we have found the solution.
        n = len(nums)
        k = n - k

        def quickSelect(l: int, r: int) -> int:
            p = l
            pivot = r
            for i in range(l, r):
                if nums[i] <= nums[pivot]:
                    # swap elements at i and p
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[pivot] = nums[pivot], nums[p]

            # Recursively continue based on which half you would find index k
            if k < p:
                return quickSelect(l, p-1)
            elif k > p:
                return quickSelect(p+1, r)
            else:
                # Indicates k == p
                # Remember in every iteration element at p is in its correct sorted position.
                return nums[k]

        return quickSelect(0, n-1)

# Time complexity: O(n) - average case. Average case is when pointer p ends up in middle in every iteration,
#                  splitting nums into exact half. n + n/2 + n/4 = O(n)
#                  O(n^2) - worst case. Worst case is when p is either at left or right end, which leads to n comparison
#                  in each iteration.
# Space complexity: O(n)
        '''

        # The following approach works, but one teste case is exceeding time limit, maybe because of worst case time 
        # complexity of O(n^2). hence, solving the same using minheap
        minHeap = []

        # Iterate through given nnumber and maintain a min heap of size k
        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # Element at root is Kth largest value 
        return minHeap[0]

# Time complexity: O(nlogk)
# Space complexity: O(k)