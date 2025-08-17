class TimeMap:

    def __init__(self):
        # Dict key will represent key
        # Dict values will be list of tuples: [(val1, time1), (val2, time2)]
        self.keyStore=dict()   


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key]=[]
        self.keyStore[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        valList=self.keyStore.get(key, [])
        
        # Since list is sorted with respect to time, binary search can be applied to find the time
        l,r = 0, len(valList)-1
        while l<=r:
            mid=(l+r)//2
            if valList[mid][1]==timestamp:
                # If exact time stamp is found, return the value
                return valList[mid][0]
            
            if timestamp>valList[r][1]:
                # If timetsamp is greater than r, then return value at r (requirement)
                return valList[r][0]
            
            if timestamp<valList[l][1]:
                # If timestamp is less than l, then return value before l if it is present
                val=valList[l-1][0] if l>0 else ""
                return val
            
            if timestamp<valList[mid][1]:
                r=mid-1
            elif timestamp>valList[mid][1]:
                l=mid+1
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)