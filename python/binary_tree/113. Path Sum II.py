# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.traverse(root, targetSum, deque())
        return self.res


    def traverse(self,root:Optional[TreeNode],targetSum:int,path:deque):
        if not root:
            return

        path.append(root.val)               # ① 先把当前节点加入路径
        remain = targetSum - root.val       # ② 更新剩余目标

        # ③ 到达叶子节点
        if not root.left and not root.right:
            if remain == 0:
                self.res.append(list(path)) # 复制一份当前路径

        # ④ 继续递归左右子树
        self.traverse(root.left, remain, path)
        self.traverse(root.right, remain, path)

        path.pop()                          # ⑤ 回溯，撤销当前节点