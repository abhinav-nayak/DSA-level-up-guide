class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use two pointer approach to check for palindrome
        i, j = 0, len(s)-1
        while i<=j:
            # ignoring non-alphanumeric characters. We can use .isdigit() or .alpha() also separately.
            while i<=j and not s[i].isalnum():
                i += 1
            while i<=j and not s[j].isalnum():
                j -= 1
            
            if i<=j and s[i].lower()!=s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True

# Time complexity: O(n)
# Space complexity: O(1)