class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashSet to check for duplicates in O(1)
        hashSet=set()

        # Dynamic sliding window approach as we have to find longest substring
        longest=0
        l,r = 0,0
        while r<len(s):
            if s[r] in hashSet:
                hashSet.remove(s[l])
                l+=1
            else:
                longest=(r-l+1) if (r-l+1)> longest else longest
                hashSet.add(s[r])
                r+=1

        return longest

# Time complexity: O(n) 
# Space complexity: O(m)
# where n is the length of the string and m is the number of unique characters in the string