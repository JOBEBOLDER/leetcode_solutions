class Solution:
    #mdeium
    #binary search:求最小
    #关键写一个check函数
    #time:Ologn
    #space:O1
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            mid = left + (right - left) // 2
            res = self.check(nums, mid)

            if res > threshold:
                left = mid + 1
            elif res <= threshold:
                right = mid #mid is answer probably
        return left


    def check(self, nums:List[int], divisor:int) -> int:
        sum = 0

        for num in nums:
            sum += math.ceil(num / divisor)
        return sum