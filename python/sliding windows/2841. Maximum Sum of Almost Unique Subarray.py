class Solution:
    # medium
    # sliding window, hashtable
    # must be a subarray, so must be continuous
    #
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        left = 0
        max_sum = 0
        curr_sum = 0
        # 使用字典来跟踪窗口中每个元素的出现次数
        window_count = {}
        
        for right in range(len(nums)):
            # 添加右边界元素到窗口
            curr_sum += nums[right]
            #这个就是计数我的窗口内有多少个元素，比如【7317】，那就是7:2，3:1，1:1，所以元素个数就是3，distinct element就是3
            window_count[nums[right]] = window_count.get(nums[right], 0) + 1
            
            # 当窗口大小达到 k 时
            if right - left + 1 == k:
                # 如果窗口中不同元素的数量至少为 m
                if len(window_count) >= m:
                    max_sum = max(max_sum, curr_sum)
                
                # 移除窗口左边界元素
                curr_sum -= nums[left]
                window_count[nums[left]] -= 1
                if window_count[nums[left]] == 0:
                    del window_count[nums[left]]#如果元素计数变为0，从哈希表中删除该元素 左边界向右移动 left += 1
                left += 1
        
        return max_sum