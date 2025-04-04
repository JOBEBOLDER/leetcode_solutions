# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #time:On+On
    #space:Oh
    #OOP
    '''1、分别记录从根节点到 startValue 和 destValue 的路径 startPath 和 destPath。
    2、然后去除 startPath 和 destPath 的公共前缀。
    3、最后将 startPath 全部变成 U，把 startPath 和 destPath 接在一起，就是题目要求的路径了。'''

    def __init__(self):
        self.path = ''
        self.startPath = ''
        self.endpath = ''
        self.startValue = 0
        self.destValue = 0

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.startValue = startValue
        self.destValue = destValue

        # DFS 找路径
        self.dfs(root)

        # 去掉公共前缀
        m = len(self.startPath)
        n = len(self.endpath)
        p = 0
        while p < m and p < n and self.startPath[p] == self.endpath[p]:
            p += 1

        self.startPath = self.startPath[p:]
        self.endpath = self.endpath[p:]

        # 把 start 剩下路径换成 "U"
        self.startPath = 'U' * len(self.startPath)

        return self.startPath + self.endpath

    def dfs(self, root: Optional[TreeNode]):
        if root is None:
            return

        if root.val == self.startValue:
            self.startPath = self.path
        if root.val == self.destValue:
            self.endpath = self.path

        # 递归左子树
        self.path += 'L'
        self.dfs(root.left)
        self.path = self.path[:-1]  # 回溯

        # 递归右子树（你这里原本写错了）
        self.path += 'R'
        self.dfs(root.right)
        self.path = self.path[:-1]  # 回溯