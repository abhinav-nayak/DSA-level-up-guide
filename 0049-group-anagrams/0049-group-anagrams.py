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

        # frame the result data
        result = []
        for anagrams in hashMap.values():
            result.append(anagrams)
        
        return result
            