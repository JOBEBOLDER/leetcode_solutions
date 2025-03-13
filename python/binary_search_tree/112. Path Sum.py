# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #easy
    #time:On
    #Space:Oh
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        self.sum = 0
        self.traverse(root, targetSum)
        return self.res

    def traverse(self, root: Optional[TreeNode],targetSum:int):
        if root is None:
            return

        self.sum += root.val
        if root.left is None and root.right is None:
            if self.sum == targetSum:
                self.res = True

        self.traverse(root.left,targetSum)
        self.traverse(root.right,targetSum)

        self.sum -= root.val

        