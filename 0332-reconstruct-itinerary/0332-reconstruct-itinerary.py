import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        There are different airports and they are randomly linked to each other through flight tickets.
        This is similar to 'having multipe nodes and the relationship between them is not 
        hierarchical'.
        This is a hint that this is a graph problem.
        This problem is about traversing. DFS can be used. There are 2 important steps to do while
        performing DFS in this problem:
        (i) Same node can be re-visited, same edge cannot be re-visited.
        (ii) We neeed to visit neighbours that are smaller in lexical order first. This can be done,
        if we sort the adjacency list for each node. Instead of that, better approach is that we sort
        the input so that the adjacency list is automatically sorted when formed.
        When all edges are visited the result is found (Condition: if len(result) == len(tickets)+1).
        We also need to backtrack if itinerary cannot be formed with a chosen path.
        """
        # Step 1: sort the input, so that adjacency list is sorted
        tickets.sort()

        # Step 2: Create adjacency list
        adjacency_list = collections.defaultdict(list)
        for u, v in tickets:
            adjacency_list[u].append(v)
        
        result = ["JFK"]

        # Step 3: Perform DFS with 2 conditions mentioned above and backtracking
        def dfs(node: str) -> bool:
            nonlocal result

            # when all edges are visited, we have found a solution
            if len(result) == len(tickets)+1:
                return True
            
            # Itinerary cannot be formed witht his path, hence return and backtrack
            if len(adjacency_list[node]) == 0:
                return False
            
            temp = list(adjacency_list[node])
            for i, v in enumerate(temp):
                result.append(v)
                # we are selecting edge node->v, so remove from adjacency list so that it is not revisited
                adjacency_list[node].pop(i)
                if dfs(v):
                    return True
                
                # could not find an itinerary using node -> v edge, hence backtrack
                adjacency_list[node].insert(i, v)
                result.pop()

            return False

        dfs("JFK")
        return result

# Time complexity: O(E^2)
#                  Sorting takes - O(E * logE)
#                  Building adjacecny list takes - O(E)
#                  DFS where nodes can be revisited - O(E^2) as from each edge we may visit E edges.
# Space complexity: O(E)    - needed for adjacency list and result