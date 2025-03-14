# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #easy 
    # time:On
    #space:Oh
    #initialization
    def __init__(self):
        self.isbalance = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDepth(root)
        return self.isbalance
    

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case
        if root is None:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if abs(leftDepth - rightDepth) > 1:
            self.isbalance = False
        
        return 1 + max(leftDepth, rightDepth)

'''class Solution:
    def __init__(self):
        # 记录二叉树是否平衡
        self.balanced = True

    def isBalanced(self, root: TreeNode) -> bool:
        self.maxDepth(root)
        return self.balanced

    # 输入一个节点，返回以该节点为根的二叉树的最大深度
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # if not self.balanced:
        # 随便返回一个值即可，旨在结束递归
        #     return -666

        leftMaxDepth = self.maxDepth(root.left)
        rightMaxDepth = self.maxDepth(root.right)

        # 后序遍历位置
        # 如果左右最大深度大于 1，就不是平衡二叉树
        if abs(rightMaxDepth - leftMaxDepth) > 1:
            self.balanced = False

        return 1 + max(leftMaxDepth, rightMaxDepth)'''