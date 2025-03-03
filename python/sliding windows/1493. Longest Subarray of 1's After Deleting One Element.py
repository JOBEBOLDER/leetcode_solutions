class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0  # 用来计数窗口中0的个数
        max_length = 0
        
        for right in range(len(nums)):
            # 如果当前元素是0，增加0的计数
            if nums[right] == 0:
                zeros += 1
            
            # 如果窗口中0的数量超过1，移动左指针直到只剩一个0
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # 当前窗口长度是right-left+1，但因为要删除一个元素，所以减1
            max_length = max(max_length, right - left)
        
        return max_length