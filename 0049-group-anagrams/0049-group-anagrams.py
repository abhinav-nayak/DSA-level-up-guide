from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashMap to correlate freq count adn anagrams
        hashMap = defaultdict(list)
        for s in strs:
            # freq counter for 26 lower case letters
            count = [0]*26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # group anagrams under one key
            hashMap[tuple(count)].append(s)

        # return the data
        return list(hashMap.values())

# Time complexity: O(n*k) 
# Space complexity: O(n*k)
# where 'n' is total number of strings and 'k' is maximum length of a single string
