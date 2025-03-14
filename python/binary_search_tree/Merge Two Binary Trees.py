# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #easy
    #time:On+m
    #space:Oh
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.build(root1, root2)

    def build(self, root1:Optional[TreeNode],root2:Optional[TreeNode]):
        #base case
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1


         # 创建新节点，值为两个节点的值之和
        root = TreeNode(root1.val + root2.val)

        # 递归合并左右子树
        root.left = self.build(root1.left, root2.left)
        root.right = self.build(root1.right, root2.right)

        return root
