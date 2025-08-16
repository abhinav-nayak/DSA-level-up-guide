class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # This is a classic backtracking problem.
        # using recursion stack.
        # Same solution can be implemented without recursion, but we need to use stack manually.
        resultList=[]
        def generate(solnStr: str, openN: int, closeN: int):
            # base condition of recursion
            if openN==n and closeN==n:
                # found one combination
                resultList.append(solnStr)
                return
            
            if openN<n:
                generate(solnStr+"(", openN+1, closeN)

            # valid strings cannot have more closing brackets than opening
            if closeN<openN:
                generate(solnStr+")", openN, closeN+1)

        # call recursive method
        generate("", 0, 0)
        return resultList

# Time complexity: O(4^n / sqrt(n))
#                  For n nodes, the number of binary trees that can be formed is given by a formula #                  called Catalan number:
#                  C=(2n)Cn/(n+1)
#                  This number grows like: (4^n)/(n^1.5)
# Space complexity: O(n) - for recursion stack excluding reuslt list