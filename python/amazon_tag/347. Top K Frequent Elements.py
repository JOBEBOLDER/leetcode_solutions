
class Solution:
    ''' 在Python的heapq模块中，默认实现的是最小堆，也就是堆顶元素是最小的元素。代码中的关键逻辑是：

使用heappush将元素(freq, num)加入优先队列
当队列长度超过k时，使用heappop移除堆顶元素（即频率最小的元素）
这样最终保留在队列中的就是频率最高的k个元素

这个算法的巧妙之处在于：通过维护一个大小为k的最小堆，每次弹出频率最小的元素，最终堆中剩下的就是频率最大的k个元素。这比构建一个包含所有元素的最大堆然后弹出k个元素更高效。'''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_to_freq = Counter(nums)

        pq = []

        for num, freq in val_to_freq.items():
            heappush(pq, (freq, num))#pq按照freq排序
            if len(pq) > k:
                heappop(pq)

        res = []

        while pq:
            res.append(heappop(pq)[1])

        return res

'''时间复杂度：O(nlogk),Counter(nums) 需要 O(n)，n 是数组长度,heappush 操作需要 O(logk)
heappop 操作也需要 O(logk),

space:O(1)
'''