import heapq

class MedianFinder:

    def __init__(self):
        # max heap to store first half of the data
        self.max_heap = []
        # min heap to store second half of data
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        # Recall Problem 34: Median of Two Sorted Arrays. In that problem also, we partitioned
        # the data into 2 halves. We will follow a similar approach here.
        # So, we want a data structure so that we can find the last element of sorted first half
        # and first element of sorted second half to calculate median. And this data structure has 
        # to be modified based on the incoming data. This is similar to 'find maximum/ minimum 
        # frequently' kind of problem. So, hint is heap.
        # For first half use max heap and second half use min heap.
        
        # We can always insert element in first half. Then check:
        # 1) if |size of first half - size of second half| <= 1 (this is the definition of median).
        #    If this condition is not satisfied, move elements from one half to another (heap pop and push).
        # 2) Another condition is, max of first half <= min of second half (to make sure data is sorted).
        #    If not, move elements (heap pop and push). Once both conditions are satisfied, we can 
        # Calculate the median.

        # Step 1: Insert into first half
        heapq.heappush(self.max_heap, -1*num)

        # Step 2: After insertion check if the 2 conditions are satisfied
        if len(self.min_heap) > 0 and (-1*self.max_heap[0] > self.min_heap[0]):
            heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))

        max_heap_size = len(self.max_heap)
        min_heap_size = len(self.min_heap)
        if abs(max_heap_size - min_heap_size) > 1:
            if max_heap_size > min_heap_size:
                heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))
            else:
                heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))
        

    def findMedian(self) -> float:
        is_even = (len(self.max_heap) + len(self.min_heap)) % 2 == 0
        if is_even:
            median = (-1*self.max_heap[0] + self.min_heap[0])/2
        else:
            median = -1*self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]
        return median
       
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()