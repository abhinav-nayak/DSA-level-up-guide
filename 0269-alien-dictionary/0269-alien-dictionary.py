import collections

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        If we think of letters as nodes, then the relation netween them is not hierarchical,
        it is random and we are supposed to find this relationship. This is like
        'nodes are related in non-hierarchcial order' kind of problem, which indicates that
        it can be solved using graphs.
        Now if you think about it, we connect the nodes (letters) using arrows, letters in
        any language can be only in 1 order, so it will be a directed graph. Also, there cannot
        be any cycle because presence of cycle indicates there is not definite ordering of
        letter in that language. So, this is DAG (Directed Acyclic Graph), and the problme is
        about ordering of nodes. Hence, we can think of topological sort algorithm (which 
        uses DFS).
        Solution using topological sort:
        1. Create adjacency list: In given 'words' list, compare 2 words at a time. The letter
        where there is difference, a directed edge exists. Example: while comparing "hrn"
        with "hrf", we find that n is different from f, so there is a directed edge from n to f.
        Create adjacency list with this logic.
        Comparing two words is enough because comparing others words won't give us any new
        information. You can try out and see.
        2. Perform post order DFS:
        We use visited dict during DFS instead of set, to keep track of visited elmenets.
        We need dict because, when we have chosen a node in current DFS path, we set it to true
        in visited so that we can detect cycles. Once DFS is processed for a node, we mark it
        as false in visited to indicate that this node is already processed and there is no cycle
        from this node onwards.
        Why post order DFS + reversing the solution is needed:
        Suppose we have a graph:
        ------>-----
        |           |
        A --> B --> C
        If we process this graph with normal DFS, DFS might traverse in this order as well:
        A, C, B. But this is wrong because B comes before C. This is where topological sort
        comes in. We solve this problem by processing the leaf nodes first that is achieved
        by storing result during uphill of recursion stack i.e. post order DFS.
        So, result with post order DFS: C, B, A.
        Since we did post order DFS, result is in reverse order. SO, we reverse the result:
        A, B, C.
        3. Reverse the result and return.

        FYI:
        1. Cases when order is invalid: (i) While forming adjacency list, if we find out that
        a is a prefix of b and b appears first in given 'words' list, then it is invalid.
        (ii) If there is a cycle in graph, then it indicates invalid order.
        2. Note that the graph can be disconnected and in this case also we should be
        providing result and hence we need to perform DFS from every character. Repetitive
        DFS processing for a node is avoided using the visited dict, which stores false
        if a node is processed already.
        """
        # Step 1: create adjacency list
        adjacency_list = collections.defaultdict(set)
        for i in range(len(words)-1):
            # Compare words[i] and words[i+1]
            w_len, w_next_len = len(words[i]), len(words[i+1])
            min_val = min(w_len, w_next_len)
            # Handle invalid case 1. Read FYI above.
            if words[i][:min_val] == words[i+1][:min_val] and w_len > w_next_len:
                return ""
            for j in range(min_val):
                if words[i][j] != words[i+1][j]:
                    adjacency_list[words[i][j]].add(words[i+1][j])
                    break
        
        # Step 2: perform post order DFS - topological sort
        result = []
        visited = dict()
        def dfs(node: str) -> bool:
            if node in visited:
                # True indicates cycle is detected. False indiactes node is already processed.
                return visited[node]
            
            # if not processed, mark as visited as True to indicate it is included in current path.
            # This helps in cycle detection.
            visited[node] = True
            # Do not store result as this is post order DFS.
            # Perform DFS recursivel on the neighbours.
            for neighbor in adjacency_list[node]:
                if dfs(neighbor):
                    return True

            # add to result during uphill of recursion
            result.append(node)
            # mark visited as False to indicate DFS is processed for this node.
            visited[node] = False
        
        for word in words:
            for w in word:
                if dfs(w):
                    return ""
        
        # Step 3: Reverse the reuslt and return
        result.reverse()
        return "".join(result)

# Time complexity: O(N + V + E)
#                  O(N) for building adjacency list +
#                  O(V + E) for DFS
# Space complexity: O(V + E)
#                   O(V + E) for adjacency list, O(V) for recursion stack as well.
# Where V is the number of unique characters, E is the number of edges and 
# N is the sum of lengths of all the strings.
