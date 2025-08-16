class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Since operator comes later, we need to remember the operands while traversing.
        # Hence, stack is an obvious choice.

        # create a stack
        stack=[]

        # set for O(1) lookup
        operations=set(["+", "-", "*", "/"])

        for s in tokens:
            if s in operations:
                # pop operands, perform the operation and push the result back to stack
                operand2=stack.pop()
                operand1=stack.pop()

                result=0
                if s=="+":
                    result=operand1+operand2
                elif s=="-":
                    result=operand1-operand2
                elif s=="*":
                    result=operand1*operand2
                else:
                    # / operator. As mentioned in question we have to truncate towards zero.
                    # using // will round down, which behaves differently for negative numbers.
                    result=int(operand1/operand2)
                
                stack.append(result)
            else:
                # push operands to stack
                stack.append(int(s))
        
        return stack.pop()

# Time complexity: O(n)       
# Space complexity: O(n)