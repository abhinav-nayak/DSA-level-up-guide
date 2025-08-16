class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Basically at each index, we have to find the next maximum.
        # This is a type of 'next maximum/ next minimum' problem.
        # Hence, we can choose stack

        # initialize a stack.
        # Each element in stack is tuple: (<index of temp>, <temp>)
        # we need index to calculate number of days
        stack=[]

        #iterate over the input temperatures
        answer=[0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            # keep popping till the temperature is more than top of the stack
            while stack and temp>stack[-1][1]:
                t=stack.pop()
                answer[t[0]]=i-t[0]
            
            # Append the temp to stack
            stack.append((i, temp))
        
        # Remaining elements in the stack are inincreasong order such that there are no warmer days.
        # Hence, default value of 0 is valid
        return answer

# Time complexity: O(n)
# Space complexity: O(n)