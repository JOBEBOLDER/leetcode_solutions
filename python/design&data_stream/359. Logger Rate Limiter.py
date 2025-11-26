class Logger:

    def __init__(self):
        self.map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        #if we haven't seen this message before:
        if message not in self.map:
            self.map[message] = timestamp
            return True
        #if not enough time passed:
        if timestamp - self.map[message] >= 10:
            #update the latest time to the map:
            # 如果上次打印它的时间是 last，
            # 那这次的时间 timestamp 必须 ≥ last + 10 才能打印。

            self.map[message] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)