class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        This problem is of Palindrome pattern (recall the top 5 dynamic programming pattern).
        Once we find that a particular sub-string is palindrome, further we just need to check if the
        extra char added to left and right side is same to check if the new string is palindrome. This 
        satisfies optimal sub-structure. To check if string "dbcbd" is palindrome we need to find if 
        sub-string "bcb" is palindrome and to check if string "ddbcbdd" is palindrome we need to know if 
        string "dbcbd" is palindrome or not and for that we need to again know if "bcb" is palindrome or
        not. Hence, this satisifes overlapping solution as well.
        Hence, this can be solved using Dynamic Programming.
        Multiple palindrome sub-string can exist in the given string. Palindrome sub-string can have middle
        character at any index. Hence, iterate over the given string and at each index check how many 
        palindrome sub-string can be formed with that index as middle character of the sub-string. At each 
        index check for odd length palindromic sub-string as well as even length.
        Iterate through the given string, and while iterating consider each index as midpoint of an 
        unknown substring and go on adding chars from left and right side to find all possible
        palindrome substring with that index as midpoint. Perform the same with every index as midpoint.
        NOTE: from each index as midpoint there can be odd length palindrome substring as well as even.
        So to search for even substring, we need to start the second pointer one index ahead. So, run the
        same logic twice.
        """
        total_pali_substr = 0

        # for every index as midpoint of the possible palindromic sub-strings, find the number of palindromic
        # sub-strings
        for i in range(len(s)):
            # find odd length palindromic sub-string
            x, y = i, i
            while x>=0 and y<len(s) and s[x]==s[y]:
                total_pali_substr += 1
                x -= 1
                y += 1

            # find even length palindromic sub-string
            x, y = i, i+1
            while x>=0 and y<len(s) and s[x]==s[y]:
                total_pali_substr += 1
                x -= 1
                y += 1
        
        return total_pali_substr

# Time complexity: O(n^2)
# Space complexity: O(1)
