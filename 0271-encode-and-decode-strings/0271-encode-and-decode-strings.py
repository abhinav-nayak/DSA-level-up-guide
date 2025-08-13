class Solution:

    def encode(self, strs: List[str]) -> str:
        # prefix with string for each string - that can be the encoding algorithm
        encodedString = ""
        for s in strs:
            # delimitor is important as numbers can also be there in input string
            encodedString = encodedString + str(len(s)) + "#" + s

        print(encodedString)
        return encodedString


    def decode(self, s: str) -> List[str]:
        # perform reverse operation of encode algorithm used above
        resultList = []
        i=0
        while(i<len(s)):
            # find length of individual string with the help of delimiter
            lengthStr = s[i]
            i = i+1
            while s[i] != "#":
                lengthStr = lengthStr + s[i]
                i = i+1
            length = int(lengthStr)
            i = i+1

            # form the individual string
            indString=""
            while length>0:
                indString += s[i]
                length -= 1
                i += 1
            resultList.append(indString)

        return resultList

# Time complexity: O(m) -> for encode and decode
# Space complexity: O(m+n) -> for both encode and decode
# where m is the sum of lengths of all the strings and n is the number of strings
