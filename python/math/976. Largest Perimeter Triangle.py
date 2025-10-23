class Solution:
    #时间 O(n\log n)，空间 O(1)（若原地排序）。
    def largestPerimeter(self, nums: List[int]) -> int:
        #first have to know about the rules of forming a triangle
        #secondly:the brute force will be try to come up with all the possible solution mand return the largest one
        #base case:
        #what are the reasons that we can not form a triangle?
        #don't have 3 length
        if len(nums) < 3:
            return 0
        
        nums.sort()
        #any two sides of the lengths sum up must larger than the third side:
        for i in range(len(nums) - 1,1,-1):
            a,b,c = nums[i-2],nums[i-1],nums[i]
            if a + b > c:
                return a+b+c
        return 0
