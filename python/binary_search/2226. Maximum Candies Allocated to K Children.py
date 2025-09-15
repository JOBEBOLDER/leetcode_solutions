class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # 可选的快返回：总糖 < k，连每人 1 颗都不够
        if sum(candies) < k:
            return 0

        # 二分答案：每个孩子能拿到的糖数 x
        # 不取 0 作为被除数，左闭右开更好维护不变量：
        # check(left) == True，check(right) == False
        left, right = 1, max(candies) + 1

        def check(x: int) -> bool:
            # 能切出的 x 颗糖子堆的总个数
            return sum(c // x for c in candies) >= k

        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):          # 可行 -> 往更大的答案试
                left = mid
            else:                   # 不可行 -> 缩小到左侧
                right = mid

        return left
