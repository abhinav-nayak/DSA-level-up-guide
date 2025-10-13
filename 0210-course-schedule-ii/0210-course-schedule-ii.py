class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
                and courses cannot be completed. Once all prequisties of a course is completed, we can
                tell the current course can also be completed.
        Thi is nothing but 'topological sort' algorithm.
        """
        result = set()
        result_list = []
        visited = set()

        # Step 1: create adjacency list
        adjacency_map = {i: set() for i in range(numCourses)}
        for u, v in prerequisites:
            adjacency_map[u].add(v)
        
        # DFS implementation
        def dfs(c: int) -> bool:
            if c in visited:
                return False
            if adjacency_map[c] == set():
                if c not in result:
                    result.add(c)
                    result_list.append(c)
                return True
            
            visited.add(c)
            for dc in adjacency_map[c]:
                if not dfs(dc):
                    return False
            
            visited.remove(c)
            adjacency_map[c] = set()
            if c not in result:
                result.add(c)
                result_list.append(c)
            return True

        # Step 2: perform DFS traversal from each course
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return result_list

# Time complexity: O(V+E)
# Space complexity: O(V+E)
# where V is the number of courses and E is the number of prerequisites.