class Solution:
    #time:On
    #space: O1
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #use two pointer :
        #slow and fast pointer,slow ,fast,fast recongnize it's even number and then switch the slow pointer number
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] % 2 == 0:# 只在偶数时交换
                nums[fast],nums[slow] = nums[slow],nums[fast]
                slow += 1
        return nums