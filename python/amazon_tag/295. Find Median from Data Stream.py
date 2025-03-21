class MedianFinder:
    #time:addnum：O(log n)，findMedian 方法：O(1)
#只需要访问堆顶元素，是常数时间操作，总体空间复杂度：O(n)

#其中 n 是数据流中的元素数量两个堆 small 和 large 总共存储了所有的 n 个元素

    def __init__(self):
        #小顶堆，梯形数据
        self.large = []

        #大顶堆，正三角数据
        self.small = []

    def addNum(self, num: int) -> None:
        if len(self.small) >= len(self.large):
            heapq.heappush(self.small,-num)
            heapq.heappush(self.large, -heapq.heappop(self.small))
        else:
            heapq.heappush(self.large,num)
            heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:
        # 如果元素不一样多，多的那个堆的堆顶元素就是中位数
        if len(self.large) < len(self.small):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0] + (-self.small[0])) / 2.0
        


'''因为heapq在python里面，默认最小堆，这与 Python 的 heapq 模块的工作方式有关。heapq 模块默认只提供小顶堆（最小元素在堆顶），但在这个算法中，我们需要同时使用小顶堆和大顶堆。
为了用 heapq 实现大顶堆（self.small），代码使用了一个技巧：将所有插入的值取负数存储。这样：

当使用 heapq.heappush(self.small, -num) 插入元素时，实际上是将 -num 放入堆中'''
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()