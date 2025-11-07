import collections, heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        This is like 'having few nodes and we are asked to connect them to form a relation
        that is not hierarchical' problem. This is a hint that it can be solved using graphs.
        Imaging all the points are nodes and each nodes is connected to all other nodes. Imagine
        that this is the graph. We are asked to connect all points without a cycle and minimum 
        number of edges. This is nothing but spanning tree of a graph. They have also asked the
        'minimum cost' to form the spanning tree, which is nothing but 'Minimum Spanning Tree'
        (MST). To find MST, we have 2 algorithms: (i) Prim's algorithm (ii) Kruskal's algorithm.
        Here we will be implementing Prim's algorithm as it is easy and more efficient most
        times.
        Prim's algorithm is very similar to Dijkstra's algorithm but with a minor difference.
        Working of Prim's algorithm:
        1. Add source node (pick any node as source node here) to min heap. Min heap stores a 
        tuple: (distance to neighbouring nodes from current node, node).
        This is the exact point of difference compared to Dijkstra's algorithm. In Dijkstra's
        the tuple stores: (distance to every node from source, node)
        2. Till the time heap is non-empty:
        (i) Pop a node from min-heap (this way we always pick the node with shortest path)
        (ii) if popped node is not visited: Mark it as visited. Push non-visited neighbours to 
        the min heap. If popped node is visited: ignore.
        3. Once heap is empty, check if all nodes are visited. If all nodes are not visited, then
        all nodes cannot be reached.
        """
        def manhattan_distance(l1: List[int], l2: List[int]) -> int:
            return abs(l1[0] - l2[0]) + abs(l1[1] - l2[1])

        # Step 1: Create an adjacency list of imaginary graph
        adjacency_list = collections.defaultdict(list)
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i==j:
                    continue
                adjacency_list[i].append((manhattan_distance(p1, p2), j))
        
        # Step 2: Perform Prim's algorithm
        min_cost = 0
        visited = set()
        # Add any node
        min_heap = [(0, 0)]
        while min_heap:
            d, v = heapq.heappop(min_heap)
            if v in visited:
                continue

            # v is not visited
            min_cost += d
            visited.add(v)
            for dist, neighbour in adjacency_list[v]:
                if neighbour not in visited:
                    heapq.heappush(min_heap, (dist, neighbour))
        
        return min_cost

# Time complexity: O(n^2 * log n)
#                  Each node can be connected to n-1 other nodes. So, there can be n^2 items in #                  heap. Each heap operation is O(log n^2). And we might have to perform n^2 #                  operations.
# Space complexity: O(n^2)  - for adjacency list