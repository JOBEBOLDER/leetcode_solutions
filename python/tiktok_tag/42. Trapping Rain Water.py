class Solution:
    #two pointer
    #time:On
    #space:O1
    def trap(self, height: List[int]) -> int:
        #initialization:
        left = 0
        right = len(height) - 1

        water = 0

        l_max = height[left]
        r_max = height[right]

        while left < right:
            if l_max < r_max:#只能计算小的柱子去接水
                left += 1
                l_max = max(l_max, height[left])
                water += l_max - height[left]
            else:
                right -= 1
                r_max = max(r_max, height[right])
                water += r_max - height[right]

        return water

