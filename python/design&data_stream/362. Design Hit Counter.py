class HitCounter:
    '''
    HitCounter一直加时间timestamp，在queue里面，如果queue里面最左边时间-300s，超过了，证明expired了
    所以一直popleft把它们从最左边去掉
    
    '''
    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0] >=300:
            self.queue.popleft()
        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)