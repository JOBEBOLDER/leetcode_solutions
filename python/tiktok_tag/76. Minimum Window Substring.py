from collections import Counter

class Solution:
    '''Time
        O(N) : Each character enters and exits the window at most once
        Space
        O(1) :Only 26 characters (lowercase) tracked
        '''
    def minWindow(self, s: str, t: str) -> str:
        # Base case
        if len(t) > len(s):
            return ""
        
        cnt_s = Counter()
        cnt_t = Counter(t)
        left = 0
        ans_left, ans_right = -1, len(s)

        for right, char in enumerate(s):
            cnt_s[char] += 1  # Expand right side

            # Try to shrink window from the left if valid
            while cnt_s >= cnt_t:
                # Update the result window if this one is smaller
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right 

                cnt_s[s[left]] -= 1  # Shrink left side
                left += 1

        return "" if ans_left < 0 else s[ans_left : ans_right + 1]