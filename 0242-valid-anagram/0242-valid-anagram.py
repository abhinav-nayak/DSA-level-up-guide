from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, then it cannot be anagram
        if len(s) != len(t):
            return False
        
        hashMap = defaultdict(int)
        for i in range(len(s)):
            hashMap[s[i]] += 1
            hashMap[t[i]] -= 1
        
        for key in hashMap:
            if(hashMap[key] != 0):
                return False
        
        return True