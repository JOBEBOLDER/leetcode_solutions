# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode],x = 0) -> int:
        #medium
        #base case:
        if root is None:
            return 

        x = x * 10 + root.val

        if root.left is None and root.right is None:
            return  x

        return self.sumNumbers(root.right,x) + self.sumNumbers(root.left, x)