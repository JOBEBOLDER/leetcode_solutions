# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #time:On^2
    #space:Oh
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums,0,len(nums) -1)


    def build(self,nums,low,high):
        if low > high:
            return None

        maxval = float('-inf')
        #get the maxnum for root (we need root to build the tree)
        #	•	在 nums[low:high+1] 之间找最大值，最大值成为当前子树的根节点。
	    #. •	同时记录 index，这个位置用来切分左右子树。
        #index 是 每次递归中局部最大值的位置，它在每一层递归中都会重新计算，因为你每次处理的子数组不一样！
        for i in range(low,high + 1):
            if nums[i] > maxval:
                maxval = nums[i]
                index = i

        root = TreeNode(maxval)
        root.left = self.build(nums,low,index - 1)
        root.right = self.build(nums,index + 1, high)

        return root
            