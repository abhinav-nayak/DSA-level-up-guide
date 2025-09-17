class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Since we have to find multiple partitions such that substrings are palindrome, we can use backtracking
        result = []

        partition = []
        def dfs(i: int):
            # if we have reached the end, append to result
            if i >= len(s):
                result.append(partition.copy())
                return
            
            # check if s[i:j+1] is palindrome. If yes, continue further to search substring that are palindrome.
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        
        dfs(0)
        return result
        
    def isPalindrome(self, s: str, i: int, j: int):
        """
        Checks if the provided string is palindrome
        """
        palindrome = True
        while i <= j:
            if(s[i] != s[j]):
                palindrome = False
                break
            i += 1
            j -= 1
        return palindrome

# Time complexity: O(n * 2^(n)) - 2^(n) solutions and each solution will have n characters
# Space complexity: O(n) - recursion stack
#                 : O(n * 2^(n)) - for storing result