class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #time:On^2
        #space:On
        #base case:
        if len(nums) <= 1:
            return 1

        #dp initialization
        dp= [1] * len(nums)
        result = 1

        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

                result = max(dp[i],result)

        return result