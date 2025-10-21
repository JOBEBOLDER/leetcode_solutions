class Solution:
    #time:On
    #space:On
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        max_val = max(freq.values())
        ans = 0

        for v in freq.values():
            if v == max_val:
                ans += v
        return ans