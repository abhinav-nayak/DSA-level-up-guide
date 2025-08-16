class Solution:
    def isValid(self, s: str) -> bool:
        valid=True
        openingSet = set(["(", "{", "["])

        # It is a case of deferred matching - we can use satck here
        stack=[]

        for c in s:
            if c in openingSet:
                # push opening brackets to stack
                stack.append(c)
            else:
                if len(stack)==0:
                    # if stack is empty, no brackets to pop indicating more closing parentheses
                    valid=False
                    break
                
                # pop the opening bracket and check for match
                opening=stack.pop()
                # we can create a dict of brackets for cleaner if block
                if not (c==")" and opening=="(" or c=="}" and opening=="{" or c=="]" and opening=="["):
                    # wrong closing bracket type
                    valid=False
                    break
        
        if len(stack)!=0:
            # indicates more number of opening brackets
            valid=False
        
        return valid

# Time complexity: O(n)
# Space complexity: O(n)