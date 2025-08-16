class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # prev car cannot overtake the next car. If prev car is faster,
        # it can reach next car and move laong with it. They kind of become 1.
        # Prev element is limited by next element. From this clue, we can think of stack.

        # first we have to sort car by starting point to figure out which car cannot overtake which car
        sortedList = sorted(zip(position, speed))

        # initialise stack to store time taken by cars to reach target
        stack=[]
        for pos, sp in sortedList:
            # calculate time taken by car i to reach target
            time=(target-pos)/sp

            # If time taken by car i is greater than time taken by car in top of stack,
            # that means top of stack car is faster and eventually come adn meet car i and
            # they will become a fleet. Hence, pop until the condiiton is satisfied.
            while stack and time>=stack[-1]:
                stack.pop()
            
            # Now either stack is empty or time taken by car i is less than car at top of stack.
            # Hence car at top of stack can never reach car i, so they will be different fleet and hence push to stack
            stack.append(time)
        
        # number of fleets is nothing but length of stack
        return len(stack)

# Time complexity: O(nlogn)
# SPace complexity: O(n)