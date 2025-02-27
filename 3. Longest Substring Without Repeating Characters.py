class Solution:
    #medium
    #sliding window
    #time:On,space:On
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        res = 0
        count = {}
        right = 0

        while right < len(s):
            d = s[right]
            count[d] = count.get(d,0) + 1

            right += 1

            while count.get(d) > 1:
                c = s[left]
                count[c] -= 1
                left += 1

            res = max(res, right - left)

        return res

            

        