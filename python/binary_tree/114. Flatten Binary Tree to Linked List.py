# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        #medium
        """
        Do not return anything, modify root in-place instead.
        """
            # 基本情况
        if not root:
            return None
        
        # 1. 先分别展平左右子树
        self.flatten(root.left)
        self.flatten(root.right)
        
        # 2. 记住右子树
        right = root.right
        
        # 3. 将左子树接到右子树位置
        root.right = root.left
        root.left = None
        
        # 4. 找到当前右子树末尾
        curr = root
        while curr.right:
            curr = curr.right
        
        # 5. 将原来的右子树接到末尾
        curr.right = right