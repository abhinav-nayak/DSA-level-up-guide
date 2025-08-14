class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a hash set for O(1) lookup
        hashSet = set()
        for n in nums:
            hashSet.add(n)
        
        # hashSet to keep tarck of visited elements
        visited = set()

        # find the longest sequence length
        maxLength=0
        for n in nums:
            # skip already visisted elements
            if n in visited:
                continue

            # attempting to find a sequence
            count=0
            ele=n
            while ele in hashSet:
                visited.add(ele)
                count+=1
                ele -= 1
            
            ele=n+1
            while ele in hashSet:
                visited.add(ele)
                count+=1
                ele+=1
            
            maxLength = count if count>maxLength else maxLength
        
        return maxLength

# Time complexity: O(n)
# Space complexity: O(n)
        