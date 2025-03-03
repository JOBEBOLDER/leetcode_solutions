class Solution:
    #use two binary search
    #left bound,right bound
    #time: 这个算法使用了两次二分查找，每次二分查找的时间复杂度是 O(log n)
    #两次 O(log n) 的操作，最终时间复杂度仍然是 O(log n)，而不是 O(n log n)
    #space: O1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.left_bound(nums, target), self.right_bound(nums, target)]
    

    def left_bound(self, nums: List[int], target: int)->int:
        right = len(nums) - 1
        left = 0

        #有重叠是因为，left，right指针可能在同一个：nums = [5,7,7,8,8,10], target = 8，比如8，8
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = right - 1
            elif nums[mid] == target:
                right = mid - 1

        if left >= len(nums) or nums[left] != target:
            return -1
        else:
            return left

    
    def right_bound(self, nums:List[int], target: int)-> int:
        right = len(nums) - 1
        left = 0

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = right - 1
            elif nums[mid] == target:
                left = mid + 1

        if right < 0 or nums[right] != target:
            return -1

        else:
            return right

