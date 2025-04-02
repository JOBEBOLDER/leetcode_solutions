class Solution:
    #time:On * (amount)
    #space:On*(amount)
    #answer from neetcode solution:https://www.youtube.com/watch?v=H9bfqozjoqs
    def coinChange(self, coins: List[int], amount: int) -> int:
        #initialization of the dp table:
        #to find min,we need to set up a max value:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for sub_amount in range(1,amount + 1):
            for coin in coins:
                if sub_amount - coin >= 0:
                    dp[sub_amount] = min(dp[sub_amount],dp[sub_amount - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1