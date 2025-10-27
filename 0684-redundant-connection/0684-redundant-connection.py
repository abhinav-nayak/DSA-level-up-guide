class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Definition of tree: Graph with single connected component + no cycle.
        This basically now becomes a cycle detection kind of problem. Previously we had detected 
        cycles using DFS. Here, we can use union find algorithm (also called disjoint set 
        algorithm) to detect a cycle.
        NOTE: For a tree with N node we will always have N-1 edges. This problem says,
        a tree is initially present and addition of 1 more edge is creating a cycle. And it is 
        also given that the the additional edge is not duplicate and is not from u-v (meaning, 
        not self loop). In that case, no. of given edges = no. of nodes.
        Using this as no. of nodes we can perform union find algorithm:
        We create an instance of the DSU object and traverse through the given edges. For each 
        edge, we attempt to connect the nodes using the union function. If the union function 
        returns false, indicating that the current edge forms a cycle, we immediately return that 
        edge.
        """
        # number of nodes = no. of edges - as described above
        n = len(edges)

        # parent array to keep track of parent node of each node.
        # For node i, parent[i] is the parent node.
        # To begin with each node is its own parent
        # n+1 as nodes start from 1, not 0
        parent = [i for i in range(n+1)]

        # rank array to keep track of rank of the tree so that we can find which is smaller tree
        # while performing union.
        rank = [1 for _ in range(n+1)]

        # implementation of union-find algorithm
        def find(node: int) -> int:
            curr = node
            while curr != parent[curr]:
                # path compression for code efficiency
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr


        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                # indicates both n1 and n2 are already connected. Return Flase to indicate no union
                return False
            
            # union them as they do not belong to same component
            if rank[p1] <= rank[p2]:
                rank[p2] += rank[p1]
                parent[p1] = p2
            else:
                rank[p1] += rank[p2]
                parent[p2] = p1
            
            # return True to indicate union successful
            return True


        for u, v in edges:
            if not union(u, v):
                # indicates a cycle is formed
                return [u, v]

# Time complexity: O(V + (E * α(V)))
#                  O(V) -> to form rank and parent array
#                  O(E * α(V)) -> for each edge we perform union and find.
#                  Total time complexity is almost same as O(V + E)
# Space complexity: O(V)
# Where V is the number of vertices and E is the number of edges in the graph. 
# α() is used for amortized complexity.