class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since input is sorted, we can go for two pointer approach.
        # this also has better space complexity than solving this using hashing
        
        result=[]

        # using converging two pointer approach
        i, j=0, len(numbers)-1
        while i<j:
            sum=numbers[i]+numbers[j]
            if sum>target:
                j -= 1
            elif sum<target:
                i += 1
            else:
                # we have found the pairs
                result = [i+1, j+1]
                break
        
        return result

# Time complexity: O(n)
# Space complexity: O(1)
        