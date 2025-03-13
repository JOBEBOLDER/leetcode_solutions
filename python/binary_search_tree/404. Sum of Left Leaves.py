# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #easy
    #time:On
    #space:O1
    def __init__(self):
        self.sum = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #base case
        if root is None:
            return 0
        self.traversal(root)
        return self.sum

    def traversal(self, root:Optional[TreeNode]):
        #base case:
        if root is None:
            return 0

        # conditions :
        #那么判断当前节点是不是左叶子是无法判断的，必须要通过节点的父节点来判断其左孩子是不是左叶子。
        if root.left and root.left.left is None and root.left.right is None:
            self.sum += root.left.val

        self.traversal(root.left)
        self.traversal(root.right)
        