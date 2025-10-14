class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        As mentioned in question, it is a graph problem.
        A graph is a tree if it is acyclic, has undirected edges, is a single component and
        there exists only 1 path between 2 nodes (basically no cycles).
        To verify if it is acyclic and is made of single compoenent, represent given edges
        in the form of adjacency list. Then perform DFS traversal for cycle detection.
        We start DFS from node 0, assuming -1 as its parent. We initialize a hash set visit
        to track the visited nodes in the graph. During the DFS, we first check if the current
        node is already in visit. If it is, we return false, detecting a cycle.
        Otherwise, we mark the node as visited and perform DFS on its neighbors,
        skipping the parent node to avoid revisiting it. After all DFS calls,
        if we have visited all nodes, we return true, as the graph is connected.
        Otherwise, we return false because a tree must contain all nodes.
        """
        # Hash set to keep track of visited nodes during DFS traversal
        visited = set()
        # Hash set to keep track of visited nodes across all DFS calls -> this approach is
        # better that setting adjacency list to empty once DFS completes - as done in Problem 87: Course Schedule
        global_visited = set()

        # Step 1: create adjacency list
        adjacency_list = {i: set() for i in range(n)}
        for u, v in edges:
            adjacency_list[u].add(v)
            adjacency_list[v].add(u)
        
        # DFS implementation
        def dfs(node: int) -> bool:
            if node in visited:
                return False
            if node in global_visited:
                return True
            
            visited.add(node)
            for neighbor in adjacency_list[node]:
                # since node->neighbor path is chosen, exclude its vice versa path for current
                # DFS cycle
                adjacency_list[neighbor].remove(node)
                if not dfs(neighbor):
                    return False
                # DFS using node->neighbor path is complete, re-add the the vice-versa path.
                adjacency_list[neighbor].add(node)
            
            visited.remove(node)
            # DFS is completed for node and hence add it to global visited list
            global_visited.add(node)
            return True

        # Step 2: Start DFS from any node - for detection of cycle
        # check if it is a single component by checking if number of visited nodes is
        # same as given nodes
        if not dfs(0) or len(global_visited)!=n:
            return False

        return True

# Time complexity: O(V+E)
# Space complexity: O(V+E)
# Where V is the number vertices and E is the number of edges in the graph.
