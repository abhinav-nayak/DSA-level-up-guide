import collections, heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        In the problem statement it is mentioned that we have a network of nodes. This indicates 
        that it is a graph problem.
        This is like calculating distance between the nodes in a graph. Recall, in Problem 92: 
        Word Ladder we had used BFS to calculate distance. Here we have weighted graph,
        so we can use a variation of BFS i.e., Dijkstra's algorithm, which is the standard graph 
        algorithm to find shortest path in a graph. Dijkstra's algorithm is nothing but BFS +
        min-heap/ priority queue.
        Though before we begin with Dijkstra's algorithm, we should create the adjacecny list.
        Working of Dijkstra's algorithm:
        1. Add source node to min heap. Min heap stores a tuple: (distance to this node from 
        source, node)
        2. Till the time heap is non-empty:
        (i) Pop a node from min-heap (this way we always pick the node with shortest path)
        (ii) if popped node is not visited: Mark it as visited. Push non-visited neighbours to 
        the min heap. If popped node is visited: ignore.
        3. Once heap is empty, check if all nodes are visited. If all nodes are not visited, then
        all nodes cannot be reached. Return -1 for this problem. If all nodes are visited, then
        last popped non-visited node denotes the shortest path to reach all nodes.
        """
        # Step 1: create adjacency list
        adjacency_list = collections.defaultdict(list)
        for u, v, w in times:
            adjacency_list[u].append((v, w))
        
        # Step 2: Dijkstra's algorithm: BFS + min heap
        path = -1
        visited = set()
        # Add source to min heap
        min_heap = [(0, k)]
        while min_heap:
            # picking the shortest path
            dist, node = heapq.heappop(min_heap)
            # mark node a visited
            if node in visited:
                continue
            path = dist

            # push non visited neighbours to heap
            visited.add(node)
            for v, w in adjacency_list[node]:
                if v not in visited:
                    heapq.heappush(min_heap, (dist + w, v))
        
        return path if len(visited) == n else -1
            
# Time complexity: O(E logV)
# Space complexity: O(E + V)
# Where V is the number of vertices and E is the number of edges
