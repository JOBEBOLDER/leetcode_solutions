class Solution:
    #time:On
    #space:On(counter?)	•	Counter 最多统计 26 个大写字母（或有限字符集） → 常数空间
    #所以虽然用了 Counter，空间复杂度依然 O(1)。
    #关键思路：表示“窗口里非最多字符的数量是否超过 k”。
    # 如果超过，就必须收缩窗口。
    # 每次都更新最大长度 res。
    def characterReplacement(self, s: str, k: int) -> int:
        #use counter, 
        #know when i shloud increase window Sized

        count = Counter()
        left = 0
        max_count = 0
        res = 0

        for right, char in enumerate(s):
            #know when i shloud increase window Sized
            count[char] += 1
            max_count = max(max_count,count[char])

            #know when i should descrease window size: right-left + 1 - maxwindow_count > k
            if right -left + 1-max_count > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res






        



