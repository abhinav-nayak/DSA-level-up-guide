from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        It is not necessary that adjacent strings need to differ by a single letter, we can skip
        few strings and also form the sequence. So, now this essentially becomes a shortest distance
        between two strings kind of problem. This is a hint that problem can be solved using graph.
        Imagine the strings as nodes of a graph. The strings that differ by a single letter are
        connected with an undirected edge. Once you have a graph, start BFS from begin string to 
        end string level by level and calculate the distance.
        NOTE: it is always better to use BFS over DFS while finding shortest distance.
        NOTE: while representing it as a graph, if we form adjacency list like we do normally:
        {str1: [str2, str3]}, then time complexity becomes slightly more. We can use wildcards
        as keys in adjacency list.
        """
        # corner case as mentioned in problem
        if endWord not in wordList:
            return 0

        # since wordList does not contain beginWord, we can add it
        wordList.append(beginWord)

        # Imagine the strings as nodes of a graph. The strings that differ by a single letter are
        # connected with an undirected edge. Create adjacency list using wildcards.
        adjacency_list = collections.defaultdict(list)
        for string in wordList:
            for j in range(len(string)):
                pattern = string[:j] + "*" + string[j+1:]
                adjacency_list[pattern].append(string)
        
        # queue to perform BFS
        q = deque()
        q.append(beginWord)

        # hash set to keep track of visited nodes during BFS
        visited = set()
        visited.add(beginWord)

        distance = 1
         # Start BFS from begin word till you find the end word
        while q:
            # perform BFS level by level
            for i in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return distance
                
                # add all enighbours of node to queue
                for j in range(len(node)):
                    pattern = node[:j] + "*" + node[j+1:]
                    for neighbour in adjacency_list[pattern]:
                        if neighbour not in visited:
                            q.append(neighbour)
                            visited.add(neighbour)

            distance += 1
        
        return 0

# Time complexity: O((m ^ 2) * n)
# Space complexity: O((m ^ 2) * n)
# where n is the number of words and m is the length of the word.