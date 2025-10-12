class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        This is a kind of problem where 'dependency is there between elements'. This is a hint that
        it can be a graph problem (dependency graph).
        Represent the courses as a graph where pre-requisites represent directional edges.
        If the graph is cyclic, that means we cannot finish all courses. To finish all courses, 
        graph should be acyclic. We can detect a cycle by running DFS from each course.

        Step 1: Create adjacency list (hash map)
                Example: {course 1: (course 2, course 3), course 3: ()}
        Step 2: Perform DFS traversal from each course
        Step 3: If an already visited element is encountered again, that indicates there is a loop
                and courses cannot be completed
        """
        # Step 1: create adjacency list
        adjacency_map = {i: set() for i in range(numCourses)}
        for u, v in prerequisites:
            adjacency_map[u].add(v)

        # set to keep track of visited elements in current DFS traversal
        visited = set()

        def dfs(c: int):
            if c in visited:
                return False
            if len(adjacency_map[c]) == 0:
                return True
            
            visited.add(c)
            for dc in adjacency_map.get(c, []):
                if not dfs(dc):
                    return False
            visited.remove(c)
            # all prerequisities of c can be completed, so we can mark adjacency_map as empty
            adjacency_map[c] = set()
            return True

        # Step 2: Perform DFS traversal from each course
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
