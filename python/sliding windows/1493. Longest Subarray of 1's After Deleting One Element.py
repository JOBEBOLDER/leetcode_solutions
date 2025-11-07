class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #when you can increase the window?
        #when allow_deletion == 1 and subarray all == 1
        #when you can descrease the window?
        #when allow_deletion == 0
        #time:On,space:O1

        left = 0
        zero_count = 0
        res = 0

        for right,x in enumerate(nums):
            #when we should increase?when we can delete the element:
            if x == 0:
                zero_count += 1

                #when shrink the window? when zero_count > 1,cuz we can only delete one element
                while zero_count > 1:
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1
            res = max(res,right - left + 1 - 1) #每一轮都需要更新因为需要删掉一个元素（通常是窗口里的那个 0），有效长度 = 当前窗口长度 − 1。

        return res
                
        
