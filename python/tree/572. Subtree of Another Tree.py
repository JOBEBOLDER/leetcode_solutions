# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
这题的正确脑内模型：两个问题，两个函数

你要把题拆成两个小问题（就像面试官希望你拆的一样）：
问题 A：两棵树是否完全相同？
→ sameTree(a,b)
问题 B：subRoot 的根可能挂在 root 的哪里？
→ 对 root 的每个节点都当一次候选起点
→ isSubtree(root, subRoot) 里做“遍历/移动窗口”

所以结构天然是：
这就是你没想到的关键：外层负责“找位置”，内层负责“比内容”。

'''
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #condition that can determine 2 ndoe are the same;
        # p.val == q.val
        # p.left = q.left
        # p.right = q.right

        if not subRoot:
            return True
        if not root:
            return False

        if self.dfs(root,subRoot):
            return True
        
        #else to find in the left and right sub tree
        return self.dfs(root.left,subRoot) or self.dfs(root.right,subRoot)


    def dfs(self,p,q):
        if p is None and q is None:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.dfs(p.left,q.left) and self.dfs(p.right,q.right)