class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp initialization:正确方式：先建“行”，每行里面再建“列”
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1,len(text2) + 1):
                if text1[i-1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]+ 1

                #因为当字符不匹配时，我们要么跳过 text1[i-1]，要么跳过 text2[j-1]，选最长的那一个。
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j - 1])

        return dp[-1][-1]