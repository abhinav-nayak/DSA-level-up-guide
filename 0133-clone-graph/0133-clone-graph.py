"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # We can perform DFS traversal on the given graph and create new nodes with the values.
        # Also, we can have a hash map to map old node to corresponding new node.
        # Hash set will help here to detect already visited node during DFS traversal,
        # as graph can be cyclic.
        hash_set = set()
        old_new_node_map = {}

        def dfs(n: Optional['Node']):
            # Base condition: if node is already visited or node does not exist
            if not n or n in hash_set:
                return
            
            # Create new node and update hash map and hash set
            new_n = Node(val=n.val)
            hash_set.add(n)
            old_new_node_map[n] = new_n
            
            # Recursively create other neighbors
            for neighbor in n.neighbors:
                dfs(neighbor)
            
            # Update neighbours of new node
            new_neighbors = []
            for neighbor in n.neighbors:
                new_neighbors.append(old_new_node_map[neighbor])
            new_n.neighbors = new_neighbors

        dfs(node)
        return old_new_node_map.get(node)
        