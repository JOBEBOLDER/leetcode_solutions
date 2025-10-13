class Solution:
    #time:	•	Each twoSumClosest() (inner two-pointer search) takes O(n) in the worst case.
    #Final time complexity: O(n²)
    #space:O1
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        #base case:
        if len(nums) < 3:
            return 0
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            res += self.twopointer(nums, i+1, target - nums[i])
        return res
        


    def twopointer(self,nums,start,target):
        low = start
        high = len(nums) - 1
        count = 0

        while low < high:
            if nums[low] + nums[high] < target:
                count = count + high - low
                low +=1
            else:
                high -= 1

        return count
