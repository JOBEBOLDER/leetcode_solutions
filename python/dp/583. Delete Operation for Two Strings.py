class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #initialize the dp table
        dp = [[0] * (len(word2) + 1) for  _ in range (len(word1) + 1)]

        #initialize the dp table and arrays:
        for i in range(len(word1) + 1):  # i表示行，应该用word1的长度
            dp[i][0] = i

        # 3. 初始化第一行（表示word1是空字符串的情况）
        for j in range(len(word2) + 1):  # j表示列，应该用word2的长度
            dp[0][j] = j
        

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    #如果两个都不一样，就删除2个，所以延续[i-1][j-1] + 2步（因为删除了2个char）
                    #如果只删除一个，延续[i][j-1] + 1步（因为删除了1个char）或者延续[i-1][j] + 1步
                    dp[i][j] = min(dp[i-1][j-1] + 2, dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[-1][-1]