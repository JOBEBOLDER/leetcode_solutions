# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #medium
    # time:On
    #space: Oh
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return  self.build(nums, 0,len(nums) - 1)
        

    def build(self, nums:List[int],low:int, high:int)->TreeNode:
        #base case:
        if low > high:
            return

        #initialize the index and max_val
        index = -1
        max_val = float("-inf")
        #to find the max value:
        for i in range(low, high + 1):
            #if i found nums[i] > max,then update the nums[i] to max,and also the right now index 
            if nums[i] > max_val:
                max_val = nums[i]
                index = i

        root = TreeNode(max_val)

        #lefttree
        root.left = self.build(nums, low, index - 1 )
        #righttree:
        root.right = self.build(nums, index + 1, high)

        return root