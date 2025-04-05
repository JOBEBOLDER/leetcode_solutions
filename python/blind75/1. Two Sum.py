class Solution:
# Time: O(n) – where n is the length of nums,lookup/insertion in the dictionary is O(1) on average.
# Space: O(n) – for storing up to n elements in the hash map
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in val_to_index:
                return [val_to_index[need],i]

            else:
                val_to_index[nums[i]] = i

        return []