class Solution:
    #dp:
    #medium
    #time and space:O(max_days)
    #dp[i] = 从第 1 天到第 i 天，总共最少需要花多少钱
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #since the days is in strictly increasing order
        max_days = days[-1]

        #dp table initializaiton
        dp = [0] * (max_days + 1)

        dp_set = set(days)# 方便判断是不是出门日

        #dp pattern:
        for i in range(1,max_days + 1):
            if i not in dp_set:#不出门，不花钱
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - 1] + costs[0],# 买1天票
                #为了防止 i-7 或 i-30 小于 0，我们可以设 dp[max(0, i - 7)] 这样写。
                dp[max(0, i - 7)] + costs[1],        # 买7天票
                dp[max(0, i - 30)] + costs[2]        # 买30天票
                )

        return dp[max_days]




        