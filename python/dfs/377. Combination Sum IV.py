class Solution:
#     Time = O(target * len(nums))
# Space = O(target)
	# •	每个 remain（0, 1, 2, … target）都会被计算 一次
	# •	每次计算要看一遍 nums，所以是 len(nums)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        memo = {}

        def dfs(remain:int):
            #find one way meet the requirement
            if remain == 0:
                return 1

            if remain < 0:
                return 0

            #memo,optimation 
            if remain in memo:
                return memo[remain]
            total = 0
            for num in nums:
                total += dfs(remain - num)

            #store the dfs result in memo, so we can use next time
            memo[remain]=total
            return total

        return dfs(target)
