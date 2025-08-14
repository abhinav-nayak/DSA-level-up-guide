class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # using hashing it will be hard to find triplets
        # we can sort the data and use two sum with two pointer approach

        # sort the array - in-place sort with O(nlogn) time
        nums.sort()

        resultSet=set()
        for k, n in enumerate(nums):
            target = -n

            # two pointer approach to find target
            i, j = k+1, len(nums)-1
            while i<j:                
                sum=nums[i]+nums[j]
                if sum>target:
                    j-=1
                elif sum<target:
                    i+=1
                else:
                    # found a triplet
                    resultSet.add((nums[k], nums[i], nums[j]))
                    i+=1

        # frame the result
        return [list(tup) for tup in resultSet]

# Time complexity: O(n^2)
# Space complexity: O(m)
# where n is length of given array and m is the number of triplets