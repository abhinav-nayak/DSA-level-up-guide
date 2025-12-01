class Solution:
    def climbStairs(self, n: int) -> int:
        """
        First check for optimal sub-structure. Optimal sub-structure means optimal solution to a
        larger problem can be found out by optimal solution to sub-problem. For this check if
        problem can be solved using recursion, if yes then large problem can be solved by 
        solving sub-problems.
        Recursion tree for n=3:
                    0   (at every step we can choose either 1 or 2 steps)
                 /     \
                1       2
              /  \     /  \
            2     3   3    4
           / \
          3   4
        Number of distinct ways to reach from 1 is = no. of ways from 2 + no. of ways from 3
                                                   = 1 + 1
        So, this pattern becomes fibonacci series.
        So, we have seen it satisfies optimal sub-structure.

        Now, in the above recursion tree you can see that we have to calculate no. of ways
        from 2 (fo example) multiple times. And this applies to other numbers as well.
        Hence, it satisfies Overlapping sub-problem. Memoization can be done (without memoization
        time complexity would be O(2^n), where n is height of tree. This is not efficient.)
        Since both Optimal sub-structure and Overlapping sub-solution is satisfied, Dynamic 
        Programming can be used. Since, the pattern is fibonacci series, 1D dynamic programming
        can be used.

        Dynamic programming can be implemented 2 ways:
        (i) Memoization (Top-Down)
        (ii) Tabulation (Bottom-Up): Recall, for bottom up we need to store next 2 elements only.
        """
        # Method 1: Memoization (Recursion)
        cache = [-1 for _ in range(n+1)]

        def dfs(num: int)->int:
            # Base conditions
            if num > n:
                return 0
            if num==n:
                return 1
            
            # Memoization
            if cache[num] == -1:
                cache[num] = dfs(num+1) + dfs(num+2)
            return cache[num]

        return dfs(0)

# Time complexity: O(n) - if you visualize and remove repeated sub-problem from the recursion
#                         tree above we are left with only n elements (i.e., height of the tree)
# Space complexity: O(n) - recursion stack = height of tree