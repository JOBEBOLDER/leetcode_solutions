class Solution:
    #time:On
    #space:On
    def rob(self, nums: List[int]) -> int:
        #handle special cases:
        if len(nums)== 0:
            return 0
        #only one house:,return itself
        if len(nums) == 1:
            return nums[0]

        #initialize dp arrays 
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        #dp pattern
        for i in range(2,len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]  # 返回最后一个房屋中可抢劫的最大金额