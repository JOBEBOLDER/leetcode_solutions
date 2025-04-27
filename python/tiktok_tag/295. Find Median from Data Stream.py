class MedianFinder:
# Time:
#   - addNum: O(log n)
#   - findMedian: O(1)
# Space: O(n)
    def __init__(self):
        self.small = []
        self.large = []
#单次 addNum 时间复杂度是 O(log n)
    def addNum(self, num: int) -> None:
        if len(self.small) > len(self.large):
            heapq.heappush(self.small, -num)
            heapq.heappush(self.large, -heapq.heappop(self.small))
        else:
            heapq.heappush(self.large,num)
            heapq.heappush(self.small, - heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()