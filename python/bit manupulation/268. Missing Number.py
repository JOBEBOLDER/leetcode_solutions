class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        #first & with the res
        res ^= n
        for i in range(len(nums)):
            res ^= i ^ nums[i]

        return res