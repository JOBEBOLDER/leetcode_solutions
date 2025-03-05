class Solution:
    #medium
    #binary search ,单调函数
        '''时间复杂度：O(n * log(sum(weights)))，其中n是包裹的数量。

        二分查找的范围是从max(weights)到sum(weights)，所以是O(log(sum(weights)))
        每次二分查找的迭代中，calculateDays函数需要遍历整个weights数组，这是O(n)
        所以总的时间复杂度是O(n * log(sum(weights)))


        空间复杂度：O(1)，只使用了常数额外空间，不会随输入规模增长。'''

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            needed_days = self.calculateDays(weights, mid)

            if needed_days > days:  # 需要的天数太多，增加容量
                left = mid + 1
            else:  # 注意题目条件：需要的天数少于或等于允许《=的天数，可以尝试减少容量，保留mid边界
                right = mid
                
        return left
    
    def calculateDays(self, weights: List[int], capacity: int) -> int:
        days = 1  # 从第1天开始
        current_load = 0
        
        for weight in weights:
            # 如果加上当前包裹会超过容量，开始新的一天
            if current_load + weight > capacity:
                days += 1
                current_load = weight
            else:
                current_load += weight
                
        return days  # 已经包含了最后一天