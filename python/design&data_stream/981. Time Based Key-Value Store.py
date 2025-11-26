class TimeMap:

    def __init__(self):
        self.map = {} ## key -> [(timestamp,value)]


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        #if existed before:
        self.map[key].append((timestamp,value)) #??? #store by the time

    def get(self, key: str, timestamp: int) -> str:
        #base case:
        if key not in self.map:
            return ""

        #if it does:
        arr = self.map[key] #first get the data
        # 用二分找 <= timestamp 的最大 index
        i = bisect.bisect_right(arr, (timestamp, chr(127))) - 1

        if i >= 0:
            return arr[i][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)