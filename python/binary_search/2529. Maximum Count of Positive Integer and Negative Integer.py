class Solution:
    #time:logn
    #space:O1

    def maximumCount(self, nums: List[int]) -> int:
        #求负数的数量
        neg = bisect_left(nums, 0)
        #求positive 's number
        pos = len(nums) - bisect_right(nums, 0)
        return max(neg, pos)

