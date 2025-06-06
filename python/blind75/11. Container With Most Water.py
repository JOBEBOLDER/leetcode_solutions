class Solution:
    #space:O1
    #time:On
    def maxArea(self, height: List[int]) -> int:
        cur_area = 0
        max_area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            cur_area = min(height[left],height[right]) * (right - left)
            max_area = max(max_area,cur_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            

        return max_area
