class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map to store frequency of each element
        freqMap = dict()
        for n in nums:
            # we can use defaultdict as well instead of doing it this way
            count = freqMap.get(n, 0)
            freqMap[n] = count+1

        # replicating bucket sort  
        # list whose index is freq and value is list of numbers with that freq
        freqList = [[] for i in range(len(nums)+1)]
        for num, count in freqMap.items():
            freqList[count].append(num)

        # Index of freqList is freq. Iterate from backwards to find top K frequent elements.
        result = []
        for i in range(len(nums), 0, -1):
            for ele in freqList[i]:
                result.append(ele)
                k -= 1
                if k==0:
                    return result
        
        return result
