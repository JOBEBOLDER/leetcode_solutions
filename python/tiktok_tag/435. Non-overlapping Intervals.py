class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #记住题目问的是需要remove，helperfunction算的是不重叠的
        n = len(intervals)
        self.calculcateIntervals(intervals)
        #减去就是需要remove的
        return n - self.count


    def calculcateIntervals(self, intervals:List[List[int]]):
        #base case:
        if not intervals:
            return 0


        #sort the intervals base on the first intervals end
        intervals.sort(key = lambda x:x[1])

        x_end = intervals[0][1]
        self.count = 1

        for inter in intervals:
            start = inter[0]
            if start >= x_end:
                self.count += 1
                x_end = inter[1]

        return self.count
