class NumArray:
    '''
    需要用数学公式验证，自己举例子验证
    
    
    '''
    def __init__(self, nums: List[int]):
        # 输入一个数组，构造前缀和
        # preSum[0] = 0，便于计算累加和
        self.preSum = [0] * (len(nums) + 1)
        for i in range(1,len(nums) + 1):
            self.preSum[i] = self.preSum[i-1] + nums[i-1]


    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)