from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # To minimize the idle time, it is best that we execute the task that has to be performed most
        # number of times. To begin with, we can create hash map to maintain count of each task.
        # And after every iteration, we want to know the task with max frequency.
        # This is a type of 'find maximum/ minimum value frequently' kind of problem.
        # This is a hint that problem can be solved using heap. Max heap in this case.
        # Once a task is executed, it cannot be executed again until it's cool down period is finished.
        # To temporarily hold off the task from executing, we can use a queue data structure.
        # Once the task with highest frequency is executed (root node of heap), it is popped and
        # enqueued into the queue along with it's next feasible execution time. Whenever we have reached
        # the feasible time, we dequeue from the queue and push it back into the heap.
        # We do this until both heap and queue are empty.

        # create hash map to count freq of each task
        hashMap = defaultdict(int)
        for task in tasks:
            hashMap[ord(task)-ord('A')] += 1
        
        # create max heap, so that we can find the task with max frequency in every iteration
        maxHeap = []
        for i in range(0, 26):
            if hashMap[i]>0:
                heapq.heappush(maxHeap, hashMap[i]*-1)
        
        # create a queue to hold task in their cool down period
        q = deque()

        # Perform the operation until both heap and queue are empty (basically all tasks are executed)
        t = 0
        while maxHeap or q:
            if q and q[0][1]==t:
                # task at the beginning of the queue has completed it's cool down period.
                # Push it back into heap.
                taskFreq, time = q.popleft()
                heapq.heappush(maxHeap, taskFreq)
            if maxHeap:
                taskFreq = heapq.heappop(maxHeap)
                taskFreq += 1 # execute it once. Since it is -ve, we add 1.
                if taskFreq < 0:
                    q.append((taskFreq, t+n+1))
            t += 1
            # If it did not enter both the above if condition indiactes it is an idle cycle
        
        return t