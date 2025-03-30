class HitCounter:
    '''	•	hit() 时间复杂度：O(1)
	•	getHits() 最坏情况下是 O(n)，但每个 timestamp 只会被加一次删一次 → 实际是 均摊 O(1)'''

    def __init__(self):
        self.queue = deque()
        #	•	用 deque() 是因为它支持高效的队头删除（popleft()）

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
        return len(self.queue)

    '''	•	self.queue[0] 是队列最前面的时间戳（最早的 hit 时间）
	•	如果这个时间比当前时间早 300 秒或更多，说明它已经过期
	•	所以我们就把它从队列中删掉（popleft()）'''


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)