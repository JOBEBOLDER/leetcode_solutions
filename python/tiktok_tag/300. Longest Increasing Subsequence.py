class Solution:
        '''🧠 那为什么 j 是 0 到 i-1？

        因为我们想知道：

        在 nums[i] 之前有哪些元素 nums[j] < nums[i]，
        可以作为 nums[i] 前面的一个元素，构成更长的递增子序列。

        所以我们要检查所有位置 j（在 i 前面），找出满足 nums[j] < nums[i] 的最长子序列长度，然后 +1。'''
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