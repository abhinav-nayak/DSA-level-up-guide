class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        It is clear from question itself that it is a graph problem.
        There are 2 ways to solve it: (i) DFS (ii) Union find (or disjoint set union) algorithm.
        Solution 1: DFS:
        Similar to previous problem (Problem 88: Graph Valid Tree), we can have 2 hash sets i.e.,
        visited and global visited and perform DFS. We can iterate though all nodes and start DFS
        only from nodes that are not present in global visited set and we can count them to find
        the number of connected components in an undireced graph.
        Solution 2: Disjoint set union:
        Initially assume you have 'n' independent nodes without any edge.
        And initialize the number of disconnected components = n.
        Iterate through all edges provided. Perform union of end vertices of each edge, if they
        are disconnected. We can say 2 nodes are disconnected if they don't have the same
        parent node. If they are disconnected, perform union by merging smaller tree with bigger
        tree. If union is performed, reduce the number of disconnected components counter by 1.
        """
        # parent array to keep track of parent node of each node.
        # For node i, parent[i] is the parent node.
        # To begin with each node is its own parent
        parent = [i for i in range(n)]

        # rank array to keep track of rank of the tree so that we can find which is smaller tree
        # while performing union.
        rank = [1 for _ in range(n)]

        # variabel to keep track of result
        no_of_connected_components = n

        def find(node: int) -> int:
            """
            Find parent of each node
            """
            curr = node
            while curr != parent[curr]:
                # performing path compression for code efficiency
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr

        def union(n1: int, n2: int) -> int:
            """
            Merges 2 trees if they are disconnected
            """
            # find parent of 2 nodes
            p1, p2 = find(n1), find(n2)
            # if they are connected, no need to merge return 0 to indicate no merge.
            if p1 == p2:
                return 0
            
            # merge smaller tree to bigger tree
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            # return 1 to indicate we have merged 2 trees
            return 1

        # Iterate though provides edges and perofrm union is they are disconnected.
        for u, v in edges:
            no_of_connected_components -= union(u, v)
        
        return no_of_connected_components

# Time complexity: O(V + (E * α(V)))
#                  O(V) -> to form rank and parent array
#                  O(E * α(V)) -> for each edge we perform union and find.
#                  Total tiem complexity is almost same as O(V + E)
# Space complexity: O(V)
# Where V is the number of vertices and E is the number of edges in the graph. 
# α() is used for amortized complexity.
