

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 利用 BST 的中序遍历特性
        self.traverse(root, k)
        return self.res

    # 记录结果
    res = 0
    # 记录当前元素的排名
    rank = 0

    def traverse(self, root: TreeNode, k: int):
        if root is None:
            return
        self.traverse(root.left, k)
        # 中序代码位置
        self.rank += 1
        if k == self.rank:
            # 找到第 k 小的元素
            self.res = root.val
            return

        self.traverse(root.right, k)

