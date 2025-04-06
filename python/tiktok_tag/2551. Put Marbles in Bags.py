from typing import List
import heapq
'''

🤯 为什么这样做能帮我们优化差值？

关键点：
	•	总和是固定的！因为你没有删掉元素，只是切来切去
所以如果你把一个很大的数字切出一段，它就可能成为最大的子数组
	•	反之，如果你切的是两个小数字，它们就更可能成为小的段

	所以，你在哪切，就直接影响最大段和最小段的值！

这段代码就用 weights[i] + weights[i+1] 来近似衡量每个切口切出来的段的大小潜力，然后：
	•	找出最“暴力”的切法（切最大和最小的地方）
	•	比较差值'''

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        
        # Step 1: 构造所有切口组合 (weights[i] + weights[i+1])
        cuts = []
        for i in range(n - 1):
            cuts.append(weights[i] + weights[i + 1])

        # Step 2: 找出最大 k-1 个 和 最小 k-1 个
        max_k = self.get_top_k(cuts, k - 1, largest=True)
        min_k = self.get_top_k(cuts, k - 1, largest=False)

        # Step 3: 分别求和后返回差值
        return sum(max_k) - sum(min_k)
    
    def get_top_k(self, arr: List[int], k: int, largest: bool) -> List[int]:
        """
        自己实现一个取 top-k 元素的函数
        如果 largest=True → 返回最大的 k 个
        如果 largest=False → 返回最小的 k 个
        """
        if k == 0:
            return []

        heap = []
        for num in arr:
            val = num if largest else -num  # 如果要最大，正常加；如果要最小，取反转成最大堆
            heapq.heappush(heap, val)
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 取出来后反转回来
        return [x if largest else -x for x in heap]