class Solution:
    '''
    📘 模板记忆法：

    遇到这类“找最大/最远的距离、满足 A[i] <= A[j]”的问题，想这三步：
	1.	先从左往右建一个“候选 i 的栈”（单调递减）
	2.	再从右往左找能配对的 j
	3.	一边配一边弹栈，记录最大 j - i
    time:On
    space:On
    '''
    def maxWidthRamp(self, nums: List[int]) -> int:
        #initialization 
         # Step 1: Build decreasing stack of indices
         #we can not miss all the poential starting point
        stack = []

        for i in range(len(nums)):
            #store the index that they are potenially the lowest point index
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        max_width = 0

        for j in range(len(nums) - 1,-1,-1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width,j-i)

        return max_width

        
