from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, then it cannot be anagram
        if len(s) != len(t):
            return False
        
        # using default dict as hash map, so that values are defaulted to 0
        hashMap = defaultdict(int)
        for i in range(len(s)):
            hashMap[s[i]] += 1
            hashMap[t[i]] -= 1
        
        # check if character count of s and t matches
        for key in hashMap:
            if(hashMap[key] != 0):
                return False
        
        return True

# Time complexity: O(n)
# Space complexity: O(1) - since only lowercase letters, max 26