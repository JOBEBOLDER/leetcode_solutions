# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #medium
    # dfs
    def __init__(self):
        self.path = ""#keep track fo the result
        self.res = None

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.dfs(root)
        return self.res

    def dfs(self, root:Optional[TreeNode]):
        #base case
        if root is None:
            return

        #end condition:
        if root.left is None and root.right is None:
            self.path = chr(ord('a') + root.val) + self.path
            s = self.path
            if self.res is None or self.res > s:
                self.res = s

            # 恢复，正确维护 path 中的元素
            self.path = self.path[1:]
            return


        # 前序位置
        self.path = chr(ord('a') + root.val) + self.path

        self.dfs(root.left)
        self.dfs(root.right)

        # 后序位置
        self.path = self.path[1:]
