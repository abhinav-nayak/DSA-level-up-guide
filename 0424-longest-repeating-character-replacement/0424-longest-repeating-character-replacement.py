from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # nested function to calculate max frequency
        def maxFreq():
            maxm=0
            for freq in hashMap.values():
                maxm=freq if freq>maxm else maxm
            return maxm

        # hash map to store frequency
        hashMap=defaultdict(int)

        longest=0

        # Dynamic sliding window approach.
        # Logic: Till the time the following condition is satisfied, we have a valid window:
        #        len(window)-max frequency of an element <= k
        l,r = 0,0
        while r<len(s):
            hashMap[s[r]]+=1
            valid=True if (r-l+1)-maxFreq()<=k else False
            if valid:
                longest=(r-l+1) if (r-l+1)>longest else longest
                r+=1
            else:
                hashMap[s[l]]-=1
                l+=1
                r+=1
        
        return longest

# Time complexity: O(n*m)
# Space complexity: O(m)
# where n is the length of the string and m is the number of unique characters in the string.