# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #easy
    #3 scenario:true：1.只有root一个点，2:左右都是空，
    #false: 左右其中一个为空，左右其中一个val不相同

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.check(root.left, root.right)

    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        # first to consider the empty root,children cases
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        # have children ,but the values are not the same
        if left.val != right.val:
            return False

        # have children and the value are equal and to iterative to check:
        return self.check(left.left, right.right) and self.check(left.right, right.left)
