import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # This is a kind of 'find maximum or minimum value' problem as we have to find
        # the K smallest distance from the origin.
        # Iterate through the given points, calculate the distance given by the formula below
        # and insert one by one into the max heap.
        # Euclidean distance is the distance between two points on X-Y plane:
        # Euclidean distance = sqrt((x1-x2)^2 + (y1-y2)^2)

        # NOTE: if we insert a list or tuple into heap, the sorting is done based on 
        # lexicographic order. Same happens when use sort or sorted methods.
        # Lexicographic order: (i) Compare the first element (ii) If equal, compare the second, 
        # then the third, and so on.

        maxHeap = []

        # Iterate by unpacking the points and insert into max heap of size k
        for x, y in points:
            dist = math.sqrt(math.pow(abs(x),2) + math.pow(abs(y),2))*-1
            # Sorting will be done by lexicographic order i.e., 1st element = dist
            heapq.heappush(maxHeap, [dist, x, y])

            # elimiate higher values
            if len(maxHeap) == k+1:
                heapq.heappop(maxHeap)

        # collect the result in a list
        result = []
        while maxHeap:
            res = heapq.heappop(maxHeap)
            result.append([res[1], res[2]])
        
        return result

# Time complexity: O(nlogk)
# Space complexity: O(k)