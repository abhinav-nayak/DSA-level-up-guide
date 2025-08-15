class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # corner case
        if len(s1)>len(s2):
            return False

        # create hash map of s1
        count1=[0]*26
        for c in s1:
            count1[ord(c)-ord("a")]+=1

        # create hash map of substring of s2. Substring length equal to length of s1.
        count2=[0]*26
        for i in range(len(s1)):
            count2[ord(s2[i])-ord("a")]+=1

        # Maintain count of matching letters
        letterCountMatch=0
        for i in range(len(count1)):
            if count1[i]==count2[i]:
                letterCountMatch+=1
        
        # sliding window apporach to find a permutation
        l=0
        for r in range(len(s1), len(s2)):
            if letterCountMatch==26:
                break

            # increment r pointer
            if count2[ord(s2[r])-ord("a")] == count1[ord(s2[r])-ord("a")]:
                letterCountMatch-=1
            count2[ord(s2[r])-ord("a")]+=1
            if count2[ord(s2[r])-ord("a")] == count1[ord(s2[r])-ord("a")]:
                letterCountMatch+=1
            
            # increment left pointer
            if count2[ord(s2[l])-ord("a")] == count1[ord(s2[l])-ord("a")]:
                letterCountMatch-=1
            count2[ord(s2[l])-ord("a")]-=1
            if count2[ord(s2[l])-ord("a")] == count1[ord(s2[l])-ord("a")]:
                letterCountMatch+=1   
            l+=1

        return letterCountMatch==26

# Time complexity: O(n)
# Space complexity: O(1)