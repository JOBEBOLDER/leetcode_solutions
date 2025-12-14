# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum = targetSum
        if root is None:
            return False
        return self.dfs(root,0)



    def dfs(self,root, cur_sum):
        if root is None :
            return False

        #	1.	进入节点时更新状态（cur_sum += root.val）——这就是 preorder 风格的“在递的过程中维护值”
        cur_sum += root.val
        #	2.	如果是叶子，立刻结算并返回
        if root.left is None and root.right is None:
            return cur_sum == self.targetSum

        #	3.	否则继续递归孩子
        return self.dfs(root.left,cur_sum) or self.dfs(root.right,cur_sum)