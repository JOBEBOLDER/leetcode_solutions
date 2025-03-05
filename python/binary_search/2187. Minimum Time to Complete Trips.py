class Solution:
    '''时间复杂度：O(n·log(m·t))，其中 n 是公交车数量，m 是最小行程时间，t 是 totalTrips
    二分查找的范围是从 1 到 min(time)·totalTrips，所以是 O(log(min(time)·totalTrips))
    每次检查需要遍历整个数组，复杂度为 O(n)
    空间复杂度：O(1)，只使用了常数额外空间'''
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        if len(time) == 0:
            return -1
        # 问自己：自变量 x 的最小值是多少？
        left = 1
        # 问自己：自变量 x 的最大值是多少？
        right = min(time) * totalTrips

        while left < right:
            mid = left + (right - left) // 2
            trips = self.check(time, mid)

            if trips >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return left


    def check(self, time:List[int],totaltime:int)->int:
        trips = 0

        for t in time:
            trips += totaltime // t
        return trips

