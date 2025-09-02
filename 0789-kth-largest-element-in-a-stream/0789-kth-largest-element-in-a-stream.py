import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # This is a kind of 'find maximum or minimum value frequently' problem.
        # This is a hint that we can use heap.
        # We can use min heap of size K, so that Kth larget is always present at root of heap.
        self.limit = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)     # O(n) time
        while len(self.minHeap) > self.limit:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.limit:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)