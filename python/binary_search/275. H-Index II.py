class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 1
        right = len(citations) + 1

        while left < right:
            mid = left + (right - left) // 2
            #	•	如果倒数第 mid 篇论文的引用数 ≥ mid，→ 说明至少有 mid 篇论文引用次数 ≥ mid（因为比它还靠后的论文更大）。
            if citations[-mid] >= mid:
                left = mid + 1

            else:
                right = mid

        return left - 1