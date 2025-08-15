class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # corner case
        if len(s)<len(t):
            return ""

        # create hash map for string t
        hashMapt=dict()
        for c in t:
            hashMapt[c]=hashMapt.get(c, 0)+1
        
        # variable to track the number of characters whose frequency should be matched
        requiredMatches=len(hashMapt)

        # create hash map for substring of s
        hashMaps=dict()

        # Dynamic sliding window apporach to find minimum length substring
        l,r = 0, 0
        currentMatches=0
        lFinal,rFinal= 0,float("inf")
        while r<len(s):
            if requiredMatches == currentMatches:
                if r-l<rFinal-lFinal:
                    lFinal, rFinal= l,r
                #increment l
                if hashMaps.get(s[l]) == hashMapt.get(s[l]):
                    currentMatches-=1
                hashMaps[s[l]]-=1
                l+=1
            else:
                hashMaps[s[r]]=hashMaps.get(s[r], 0)+1
                if hashMaps.get(s[r]) == hashMapt.get(s[r]):
                    currentMatches+=1
                r+=1

        # incase r has reached end, but still there is chance to increment l for smaller substring
        while requiredMatches == currentMatches:
            if r-l<rFinal-lFinal:
                lFinal, rFinal= l,r
            #increment l
            if hashMaps.get(s[l]) == hashMapt.get(s[l]):
                currentMatches-=1
            hashMaps[s[l]]-=1
            l+=1

        if rFinal==float("inf"):
            return ""
        
        return s[lFinal:rFinal]
