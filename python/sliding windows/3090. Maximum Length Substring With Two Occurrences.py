class Solution:
    def maximumLengthSubstring(self, s: str) -> int:      
        left = 0
        right = 0
        res = 0
        count = {}

        while right < len(s):
            c = s[right]
            count[c] = count.get(c, 0) + 1

            right += 1

            while count.get(c) > 2:
                d = s[left]
                count[d] -= 1

                left += 1

            res = max(res,right - left)

        return res



