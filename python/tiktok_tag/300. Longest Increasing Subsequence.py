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

'''follow up:
    1. Can you do it in O(n log n) time complexity?
    2. Can you do it in O(n) space complexity?
    3. Can you do it in O(1) space complexity?'''
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         #time:Onlogn          
#         #space:On
'''
    followup:   time:nlogn
    space:On
     def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # 初始化一个空数组sub，用来维护子序列的最小结尾值

        for num in nums:  # 遍历输入数组nums里的每个数
            # 使用bisect_left在sub中找第一个 >= num 的位置
            # 这个i表示num应该放到sub数组的哪个位置
            i = bisect.bisect_left(sub, num)

            if i == len(sub):  
                # 如果i正好是sub的末尾，说明num比sub里所有数都大
                # 那么可以直接加到sub末尾，子序列变长
                sub.append(num)
            else:
                # 否则，说明num可以替换掉sub[i]
                # 为什么要替换？为了让同样长度的子序列，结尾更小！
                # 这样以后更容易接上新的更大的数字
                sub[i] = num

        # 遍历完成后，sub数组的长度就是最长上升子序列的长度
        return len(sub)

        '''