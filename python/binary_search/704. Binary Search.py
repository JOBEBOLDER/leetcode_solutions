class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target :
                right = mid - 1

            elif nums[mid] == target:
                return mid

       
        return -1
               # 此时 left > right，说明所有可能的位置都已经检查过，没有找到目标值，才能返回 -1


#time :logn，binary search
#space: o1 :no extra array